from __future__ import annotations
from typing import Tuple, List, Optional, Literal, TYPE_CHECKING
from abc import ABC
import pygame as pg 

# from tile import TileMap
from core.images import load_image


if TYPE_CHECKING:
    # This is to avoid circular imports.
    from tile import TileMap


class Object(ABC):
    frame_path: Literal["str"] = None
    actions: Optional[List] = None
    slug = None
    
    def __init__(
        self, 
        pos: Tuple[int, int],
        surface: Optional[pg.Surface] = None,
        size: Optional[Tuple[int, int]] = None
        # size: Tuple[int, int] | None = None
    ) -> None:
        
        if not self.frame_path and not surface:
            raise ValueError("Must provide 'frame_path' or existing'surface'")
        
        self.frame = surface or load_image(self.frame_path, size)
        self.pos = list(pos) # frame position
        self.size = size or (self.frame.get_width(), self.frame.get_height())
    
    @property
    def rect(self):
        return pg.rect.FRect(
            self.pos[0],
            self.pos[1],
            self.size[0],
            self.size[1]
        )
            
    def update(self, objs_in_memory: List[Object], tilemap: TileMap) -> None:
        self.perform_actions(objs_in_memory)
    
    def render(self, display: pg.Surface) -> None:
        display.blit(self.frame, self.pos)
        
    def check_collisions(self, objs: List[Object]) -> List[Object]:
        objs_copy = objs.copy()
        if self in objs:
            objs_copy.remove(self) # objects can't collide with himself
        collisions = []
        
        for obj in objs_copy:
            if not self.rect.colliderect(obj.rect):
                continue
            
            collisions.append(obj)
        
        return collisions
    
    def perform_actions(self, objs_in_memory: List[Object]) -> None:
        if not self.actions:
            return 
                
        for action in self.actions:
            collisions = self.check_collisions(objs_in_memory)
            action(self, objs_in_memory, collisions)
        
        return None
    
    @property
    def can_delete(self) -> bool:
        if hasattr(self, "_can_delete"):
            return self._can_delete
        
        # out of y screen bounds.
        # return self.rect.y > 240 or self.rect.x < 0
        return False
    
    @can_delete.setter
    def can_delete(self, value: bool) -> None:
        self._can_delete = value


class MovingObject(Object):
    velocity = None
    
    def __init__(self, pos, surface=None, size = None):
        super().__init__(pos, surface, size)
        assert self.velocity, f"Must provide velocity to {self.__class__.__name__}"
    
    def update(self, objs_in_memory, tilemap):
        self.move(tilemap)
        super().update(objs_in_memory, tilemap)
    
    def move(self, tilemap: TileMap) -> None:
        raise NotImplemented(f"move method must be implemented for {self.__class__.__name__}")
    
    def _check_tiles_collisions(self, tilemap: TileMap):
        # Prevents moving objects 
        # of crossing tiles.
        # Must be called after implementing move()
        
        # Move Y
        self.pos[1] += self.velocity[1]
        collisions = self.check_collisions(tilemap.tiles_around(self.pos))
        rect = self.rect
        for collision in collisions:
            # sleep(0.1)
            if self.velocity[1] > 0:
                rect.bottom = collision.rect.top
            if self.velocity[1] < 0:
                rect.top = collision.rect.bottom
            
            self.velocity[1] = 0
            self.pos[1] = rect.y
                
        # Move X
        self.pos[0] += self.velocity[0]
        collisions = self.check_collisions(tilemap.tiles_around((self.rect.x, self.rect.y)))
        rect = self.rect
        for collision in collisions:
            if self.velocity[0] > 0:
                rect.right = collision.rect.left
            if self.velocity[0] < 0:
                rect.left = collision.rect.right
            
            self.pos[0] = rect.x
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        self.velocity[0] = 0

class StaticObject(Object):
    ...
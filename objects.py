from __future__ import annotations
import pygame as pg
from typing import Tuple, List, Optional
from abc import ABC

class Object(ABC):
    frame_path = None 
    slug = None
    
    def __init__(
        self, 
        x_pos: int,
        y_pos: int,
        size: Optional[Tuple[int, int]] = None
        # size: Tuple[int, int] | None = None
    ) -> None:
        assert self.frame_path, f"frame path not provided for {self.__class__.__name__}"
        assert self.slug, f"slug not provided for {self.__class__.__name__}"
        
        self.frame = self.frame_path
        self.frame = pg.image.load(self.frame)
        self.frame.set_colorkey((0, 0, 0))
        if size:
            self.frame = pg.transform.scale(self.frame, size)
            
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def update(self, screen: pg.Surface, objs_in_memory: List[Object]) -> None:
        self.blit(screen)
        self.check_collisions(objs_in_memory)
        
        if self.check_collisions(objs_in_memory):
            print(self.__class__, "Colidiu com ", self.check_collisions(objs_in_memory))
        
        
    @property
    def rect(self) -> pg.Rect:
        raise NotImplemented(f"rect property must be override for {self.__class__.__name__}")
    
    def blit(self, screen: pg.Surface) -> None:
        screen.blit(self.frame, (self.x_pos, self.y_pos))
        
    def check_collisions(self, objs_in_memory: List[Object]) -> None:
        objs_copy = objs_in_memory.copy()
        objs_copy.remove(self) # objects can't collide with himself
        for obj in objs_copy:
            if not self.rect.colliderect(obj.rect):
                continue
            
            self.perform_collision_action(obj)
    
    @property
    def can_delete(self) -> bool:
        if hasattr(self, "_can_delete"):
            return self._can_delete
        
        return self.y_pos > 480 or self.y_pos < 0
    
    @can_delete.setter
    def can_delete(self, value: bool) -> None:
        self._can_delete = value
    
    def perform_collision_action(self, obj) -> None:
        print(
            f"{self.__class__.__name__} doesn't have a action for {obj.__class__.__name__}"
        )
        
        return None


class MovingObject(Object):
    velocity = None
    
    def __init__(self, x_pos, y_pos, size = None):
        super().__init__(x_pos, y_pos, size)
        assert self.velocity, f"Must provide velocity to {self.__class__.__name__}"
    
    def update(self, screen, objs_in_memory):
        super().update(screen, objs_in_memory)
        self.move()
    
    def move(self) -> None:
        raise NotImplemented(f"move method must be implemented for {self.__class__.__name__}")
    
    @property
    def rect(self) -> pg.Rect:
        # Moving objects will always have new positions.
        return pg.rect.Rect(
            self.x_pos, self.y_pos, self.frame.get_width(), self.frame.get_height()
        )


class StaticObject(Object):

    @property
    def rect(self) -> pg.Rect:
        if not hasattr(self, "_rect"):
            self._rect = pg.rect.Rect(
                self.x_pos, self.y_pos, self.frame.get_width(), self.frame.get_height()
            )
        
        return self._rect
    
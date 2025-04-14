from __future__ import annotations
from typing import Tuple, List, Optional, Literal
from abc import ABC
from random import randint as r
import pygame as pg

from core.images import load_image

class Object(ABC):
    frame_path: Literal["str"] = None
    actions: Optional[List] = None
    slug = None
    
    def __init__(
        self, 
        x_pos: int,
        y_pos: int,
        surface: Optional[pg.Surface] = None,
        size: Optional[Tuple[int, int]] = None
        # size: Tuple[int, int] | None = None
    ) -> None:
        
        if not self.frame_path and not surface:
            raise ValueError("Must provide 'frame_path' or existing'surface'")
        
        # assert self.slug, f"slug not provided for {self.__class__.__name__}"
        
        self.frame = surface or load_image(self.frame_path, size)
            
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pg.rect.Rect(
            self.x_pos, 
            self.y_pos,
            self.frame.get_width(),
            self.frame.get_height()
        )
    
    def update(self, screen: pg.Surface, objs_in_memory: List[Object]) -> None:
        self.render(screen)
        self.collisions = self.check_collisions(objs_in_memory)
        # if self.collisions:
        #     print(self, self.collisions)
        self.perform_actions(objs_in_memory)
    
    def render(self, screen: pg.Surface) -> None:
        screen.blit(self.frame, (self.x_pos, self.y_pos))
        
    def check_collisions(self, objs_in_memory: List[Object]) -> List[Object]:
        objs_copy = objs_in_memory.copy()
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
            action(self, objs_in_memory, self.collisions)
        
        return None
    
    @property
    def can_delete(self) -> bool:
        if hasattr(self, "_can_delete"):
            return self._can_delete
        
        # out of y screen bounds.
        return self.y_pos > 240 or self.y_pos < 0
    
    @can_delete.setter
    def can_delete(self, value: bool) -> None:
        self._can_delete = value


class MovingObject(Object):
    velocity = None
    
    def __init__(self, x_pos, y_pos, surface=None, size = None):
        super().__init__(x_pos, y_pos, surface, size)
        assert self.velocity, f"Must provide velocity to {self.__class__.__name__}"
    
    def update(self, screen, objs_in_memory):
        super().update(screen, objs_in_memory)
        self.move()
    
    def move(self) -> None:
        raise NotImplemented(f"move method must be implemented for {self.__class__.__name__}")

class StaticObject(Object):
    ...
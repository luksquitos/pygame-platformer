from random import randint
import pygame as pg
from time import sleep
from core import colors


class LogCollisionMixin:
    """ Draws a rect when something collides with it"""
    
    log_key = pg.K_0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rect_color = (randint(1, 100), randint(1, 200), randint(1, 200))
    
    def update(self, objs, tilemap):
        super().update(objs, tilemap)
        # FIXME Objeto está sendo renderizado 
        # pelo em game.py
        self.screen = screen
        collisions = self.check_collisions(objs)
        self.draw()
        if collisions:
            ...
            # self.log()
        
    def log(self):
        # key_pressed = pg.key.get_pressed()
        # if not key_pressed[self.log_key]:
        #     return 
        
        message = (
            f"{self.__class__.__name__} "
            f"rect-x: {self.rect.x} "
            f"rect-y: {self.rect.y} "
            f"{self.rect} "
            f"top: {self.rect.top} "
            f"bottom: {self.rect.bottom} "
            f"left: {self.rect.left} "
            f"right: {self.rect.right} "
        )
            
        
        print(colors.RED + message + colors.RESET)
        sleep(0.1)
        
    def draw(self):
        pg.draw.rect(self.screen, self.rect_color, self.rect)
            
        
        
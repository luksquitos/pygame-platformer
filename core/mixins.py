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
    
    def update(self, screen, objs):
        self.screen = screen
        super().update(screen, objs)
        
    def log(self):
        key_pressed = pg.key.get_pressed()
        if not key_pressed[self.log_key]:
            return 
        
        message = (
            f"{self.__class__.__name__} "
            f"x: {self.x_pos} "
            f"y: {self.y_pos} "
            f"{self.rect} "
            f"top: {self.rect.top} "
            f"bottom: {self.rect.bottom} "
            f"left: {self.rect.left} "
            f"right: {self.rect.right} "
        )
            
        
        print(colors.RED + message + colors.RESET)
        # sleep(0.1)
        
    def draw(self):
        pg.draw.rect(self.screen, self.rect_color, self.rect)
            
    def perform_collision_action(self, obj):
        super().perform_collision_action(obj)
        self.draw()
        self.log()
        
        
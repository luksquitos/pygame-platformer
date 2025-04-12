import pygame as pg
from delay import Delay


class Rock:
    def __init__(self, x, y):
        self.frame = pg.image.load("data/images/tiles/stone/0.png")
        self.frame.set_colorkey((0, 0, 0))
        self.x_pos = x
        self.y_pos = y
        
    
    def update(self, screen, objects_in_memory):
        self.blit(screen)
        self.move()
        
    def move(self):
        self.y_pos -= 10
        
    def blit(self, screen):
        screen.blit(
            self.frame,
            (self.x_pos, self.y_pos)
        )
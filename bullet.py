import pygame as pg


class Rock:
    def __init__(self, x, y):
        self.frame = pg.image.load("data/images/tiles/stone/0.png")
        self.frame.set_colorkey((0, 0, 0))
        self.x_pos = x
        self.y_pos = y
        
    
    def update(self, objects_in_memory):
        self.move()
        
    def move(self):
        self.y_pos -= 10
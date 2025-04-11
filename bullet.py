import pygame as pg


class Rock:
    def __init__(self, player):
        self.frame = pg.image.load("data/images/tiles/stone/0.png")
        self.frame.set_colorkey((0, 0, 0))
        self.player = player
        self.x_pos = player.x_pos
        
    
    def update(self):
        self.move()
        
    def move(self):
        pass
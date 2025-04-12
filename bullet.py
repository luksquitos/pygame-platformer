import pygame as pg
from delay import Delay
from objects import MovingObject

class Rock(MovingObject):
    frame_path = "data/images/tiles/stone/0.png"
    velocity = 10
    
    def move(self):
        self.y_pos -= self.velocity

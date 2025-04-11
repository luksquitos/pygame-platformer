import pygame as pg
from random import randint

class Entity:
    frame = None
    y = None
    
    def __init__(self, x_pos):
        self.frame = pg.image.load(self.frame)
        self.frame.set_colorkey((0, 0, 0))
        self.x_pos = x_pos
        self.y_pos = self.y
        
        self.speed = 10
        
    def update(self):
        self.move()
    
    def move(self):
        # print("OI")
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_w]:
            self.y_pos -= self.speed
        
        if key_pressed[pg.K_s]:
            self.y_pos += self.speed
        
        if key_pressed[pg.K_a]:
            self.x_pos -= self.speed
        
        if key_pressed[pg.K_d]:
            self.x_pos += self.speed

class Player(Entity):
    frame = "data/images/entities/player/idle/00.png"
    y = 200
    
class Enemy(Entity):
    frame = "data/images/entities/enemy/idle/00.png"
    x = randint(100, 600)
    y = 0
    
    
    def move(self):
        self.y_pos += self.speed
        
        if self.y_pos >= 480:
            self.delete = True
        
        
    
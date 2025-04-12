import pygame as pg
from random import randint
from bullet import Rock
from delay import Delay

class Entity:
    frame = None
    y = None
    
    def __init__(self, x_pos):
        self.frame = pg.image.load(self.frame)
        self.frame.set_colorkey((0, 0, 0))
        self.x_pos = x_pos
        self.y_pos = self.y
        
        
        self.speed = 10
        self.attack_delay = None
        
    def update(self, screen, objects_in_memory):
        self.blit(screen)
        self.move()
        self.attack(objects_in_memory)
        self.get_rect()
        
    def get_rect(self):
        return pg.rect.Rect(
            self.x_pos, self.y, 
            self.frame.get_width(), 
            self.frame.get_height()
        )
        
    def attack(self, objects_in_memory: list):
        if self.attack_delay:
            return 
        
        key_pressed = pg.key.get_pressed()

        if key_pressed[pg.K_SPACE]:
            objects_in_memory.append(Rock(self.x_pos, self.y_pos))
            self.attack_delay = Delay(milliseconds=150)
            
    def blit(self, screen):
        screen.blit(
            self.frame,
            (self.x_pos, self.y_pos)
        )
    
    def move(self):
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
            
            
    def attack(self, objects_in_memory):
        return None
        
        
    
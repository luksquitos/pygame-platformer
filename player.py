import pygame as pg
from random import randint
from bullet import Rock
from delay import Delay
from objects import MovingObject


class Player(MovingObject):
    frame_path = "data/images/entities/player/idle/00.png"
    velocity = 10
    
    def update(self, screen, objs_in_memory):
        super().update(screen, objs_in_memory)
        self.attack(objs_in_memory)
    
    def attack(self, objects_in_memory: list):
        if not hasattr(self, "attack_delay"):
            self.attack_delay = None

        if self.attack_delay:
            return 
        
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_SPACE]:
            objects_in_memory.append(Rock(self.x_pos, self.y_pos))
            self.attack_delay = Delay(milliseconds=150)

    def move(self):
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_w]:
            self.y_pos -= self.velocity
        
        if key_pressed[pg.K_s]:
            self.y_pos += self.velocity
        
        if key_pressed[pg.K_a]:
            self.x_pos -= self.velocity
        
        if key_pressed[pg.K_d]:
            self.x_pos += self.velocity
    
class Enemy(MovingObject):
    frame_path = "data/images/entities/enemy/idle/00.png"
    velocity = 5
    
    @classmethod
    def generate(cls):
        from random import randint
        
        return cls(x_pos=randint(100, 400), y_pos=0)
    
    def move(self):
        self.y_pos += self.velocity
        
        if self.y_pos >= 480:
            self.delete = True
            
            
    def attack(self, objects_in_memory):
        return None
        
        
    
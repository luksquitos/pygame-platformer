import pygame as pg
import slugs
from bullet import Rock
from delay import Delay
from objects import MovingObject
from core.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT

class Player(MovingObject):
    frame_path = "entities/player/idle/00.png"
    slug = slugs.PLAYER
    velocity = 8
    
    def update(self, screen, objs_in_memory):
        super().update(screen, objs_in_memory)
        self.attack(objs_in_memory)
    
    @property
    def can_delete(self):
        return False
    
    def attack(self, objects_in_memory: list):
        if not hasattr(self, "attack_delay"):
            self.attack_delay = None

        if self.attack_delay:
            return 
        
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_SPACE]:
            objects_in_memory.append(Rock(self.x_pos, self.y_pos-20))
            self.attack_delay = Delay(milliseconds=150)

    def move(self):
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_w] and self.rect.top > 0:
            self.y_pos -= self.velocity
        
        if key_pressed[pg.K_s] and self.rect.bottom <= DISPLAY_HEIGHT:
            self.y_pos += self.velocity
        
        if key_pressed[pg.K_a] and self.rect.left > 0:
            self.x_pos -= self.velocity
        
        if key_pressed[pg.K_d] and self.rect.right <= DISPLAY_WIDTH:
            self.x_pos += self.velocity
    
class Enemy(MovingObject):
    frame_path = "entities/enemy/idle/00.png"
    slug = slugs.ENEMY
    velocity = 2
    
    @classmethod
    def generate(cls, size=None):
        from random import randint
        
        return cls(x_pos=randint(1, 200), y_pos=0, size=size)
    
    def move(self):
        self.y_pos += self.velocity
        
        if self.y_pos >= 480:
            self.delete = True
            
            
    def attack(self, objects_in_memory):
        return None
        
        
    
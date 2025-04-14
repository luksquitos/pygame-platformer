import pygame as pg
import slugs
from bullet import Rock
from delay import Delay
from objects import MovingObject
from core.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT
from core.mixins import LogCollisionMixin


def shoot_bullet(instance, objs_in_memory, collisions):
    if not hasattr(instance, "attack_delay"):
        instance.attack_delay = None

    if instance.attack_delay:
        return 
    
    key_pressed = pg.key.get_pressed()
    
    if key_pressed[pg.K_SPACE]:
        objs_in_memory.append(Rock(instance.rect.center[0], instance.rect.center[1]))
        instance.attack_delay = Delay(milliseconds=150)
    

class Player(MovingObject):
    frame_path = "entities/player/idle/00.png"
    slug = slugs.PLAYER
    velocity = 2
    direction = "idle"
    actions = [shoot_bullet]

    def move(self):
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_w] and self.rect.top > 0:
            self.rect.y -= self.velocity
            self.y_pos -= self.velocity
            
            self.direction = "up"
        
        if key_pressed[pg.K_s] and self.rect.bottom <= DISPLAY_HEIGHT:
            self.rect.y += self.velocity
            self.y_pos += self.velocity
            self.direction = "down"
        
        if key_pressed[pg.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocity
            self.x_pos -= self.velocity
            self.direction = "left"
        
        if key_pressed[pg.K_d] and self.rect.right <= DISPLAY_WIDTH:
            self.rect.x += self.velocity
            self.x_pos += self.velocity
            self.direction = "right"


def kill_player(instance, objs_in_memory, collisions):
    if not collisions:
        return 
    
    for obj in collisions:
        if obj.slug != slugs.PLAYER:
            continue
        
        obj.can_delete = True

class Enemy(MovingObject):
    frame_path = "entities/enemy/idle/00.png"
    slug = slugs.ENEMY
    actions = [kill_player]
    velocity = 2
    
    @classmethod
    def generate(cls, size=None):
        from random import randint
        
        return cls(x_pos=randint(1, 200), y_pos=0, size=size)
    
    def move(self):
        self.y_pos += self.velocity
        self.rect.y += self.velocity
        
        
    
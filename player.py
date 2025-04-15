import pygame as pg
import slugs
from bullet import Rock
from delay import Delay
from objects import MovingObject
from core.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT
from core.mixins import LogCollisionMixin
from time import sleep


def shoot_bullet(instance, objs_in_memory, collisions):
    if not hasattr(instance, "attack_delay"):
        instance.attack_delay = None

    if instance.attack_delay:
        return 
    
    key_pressed = pg.key.get_pressed()
    
    if key_pressed[pg.K_SPACE]:
        objs_in_memory.append(Rock(instance.rect.center[0], instance.rect.center[1]))
        instance.attack_delay = Delay(milliseconds=150)
    

class Player(LogCollisionMixin, MovingObject):
    frame_path = "entities/player/idle/00.png"
    slug = slugs.PLAYER
    velocity = 2
    direction = "idle"
    actions = [shoot_bullet]

    def move(self):
        key_pressed = pg.key.get_pressed()
        velocity_y = 0
        velocity_x = 0

        if key_pressed[pg.K_w]:
            velocity_y = -self.velocity
        
        if key_pressed[pg.K_s] :
            velocity_y = self.velocity

        if key_pressed[pg.K_a]:
            velocity_x = -self.velocity
        
        if key_pressed[pg.K_d]:
            velocity_x = self.velocity

        # Mexe Y
        for collision in self.collisions:
            if velocity_y > 0:
                self.rect.bottom = collision.rect.top
                velocity_y = 0
            elif velocity_y < 0:
                self.rect.top = collision.rect.bottom
                velocity_y = 0
            # sleep(0.1)
                
        # Mexe X
        for collision in self.collisions:
            if velocity_x > 0:
                self.rect.right = collision.rect.left
                velocity_x = 0
            elif velocity_x < 0:
                self.rect.left = collision.rect.right
                velocity_x = 0
            # sleep(0.1)
            
        self.rect.y += velocity_y        
        self.rect.x += velocity_x
        

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
        self.rect.y += self.velocity
        
        
    
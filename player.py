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
        objs_in_memory.append(Rock((instance.rect.center[0], instance.rect.center[1])))
        instance.attack_delay = Delay(milliseconds=150)
    

class Player(MovingObject):
    frame_path = "entities/player/idle/00.png"
    slug = slugs.PLAYER
    velocity = [0, 0]
    direction = "idle"
    actions = [shoot_bullet]
    collisions = {"up": False, "down": False, "left": False, "right": False}

    def move(self):
        key_pressed = pg.key.get_pressed()
        aceleration_x = 1        
        self.collisions = {"up": False, "down": False, "left": False, "right": False}
        
        # JUMP
        if key_pressed[pg.K_w]: 
            self.velocity[1] -= 0.5

        if key_pressed[pg.K_a]:
            self.velocity[0] = -aceleration_x
        
        if key_pressed[pg.K_d]:
            self.velocity[0] = aceleration_x

        self._check_tiles_collisions()
        

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
        
        return cls((randint(1, 200), 0), size=size)
    
    def move(self):
        self.pos[1] += self.velocity
        
        
    
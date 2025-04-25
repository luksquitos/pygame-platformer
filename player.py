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

        if key_pressed[pg.K_w]: # JUMP
            self.velocity[1] -= 0.5
        
        # if key_pressed[pg.K_s] :
        #     self.velocity[1] += 0.5

        if key_pressed[pg.K_a]:
            self.velocity[0] = -aceleration_x
        
        if key_pressed[pg.K_d]:
            self.velocity[0] = aceleration_x

        # Move Y
        self.pos[1] += self.velocity[1]
        collisions = self.check_collisions(self.tilemap.tiles_around(self.pos))
        rect = self.rect
        for collision in collisions:
            # sleep(0.1)
            if self.velocity[1] > 0:
                rect.bottom = collision.rect.top
            if self.velocity[1] < 0:
                rect.top = collision.rect.bottom
            
            self.velocity[1] = 0
            self.pos[1] = rect.y
                
        # Move X
        self.pos[0] += self.velocity[0]
        collisions = self.check_collisions(self.tilemap.tiles_around((self.rect.x, self.rect.y)))
        rect = self.rect
        for collision in collisions:
            if self.velocity[0] > 0:
                rect.right = collision.rect.left
            if self.velocity[0] < 0:
                rect.left = collision.rect.right
            
            self.pos[0] = rect.x
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        self.velocity[0] = 0
        

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
        self.pos[1] += self.velocity
        
        
    
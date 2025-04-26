import pygame as pg

import slugs
from objects import MovingObject


def kill_enemy(instance, objs_in_memory, collisions):
    if not collisions:
        return
    
    for obj in collisions:
        if obj.slug != slugs.ENEMY:
            continue
        
        obj.can_delete = True
        instance.can_delete = True

class Rock(MovingObject):
    frame_path = "projectile.png"
    actions = [kill_enemy]
    slug = slugs.BULLET
    velocity = 1
    
    def move(self):
        self.pos[1] -= self.velocity
        
        self._check_tiles_collisions()


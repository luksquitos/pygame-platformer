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

class Bullet(MovingObject):
    frame_path = "projectile.png"
    actions = [kill_enemy]
    slug = slugs.BULLET
    velocity = [0.5, 0]
    
    def move(self, tilemap):
        self.pos[0] += self.velocity[0]
        # self._check_tiles_collisions(tilemap)

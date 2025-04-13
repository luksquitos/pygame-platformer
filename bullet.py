import pygame as pg

import slugs
from objects import MovingObject


class Rock(MovingObject):
    frame_path = "projectile.png"
    slug = slugs.BULLET
    velocity = 7
    
    def move(self):
        self.y_pos -= self.velocity
        
    def perform_collision_action(self, obj):
        if obj.slug == slugs.ENEMY:
            obj.can_delete = True
            self.can_delete = True

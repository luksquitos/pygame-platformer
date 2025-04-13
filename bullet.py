import pygame as pg
import slugs
from delay import Delay
from objects import MovingObject
class Rock(MovingObject):
    frame_path = "data/images/tiles/stone/0.png"
    slug = slugs.BULLET
    velocity = 7
    
    def move(self):
        self.y_pos -= self.velocity
        
    def perform_collision_action(self, obj):
        if obj.slug == slugs.ENEMY:
            obj.can_delete = True
            self.can_delete = True

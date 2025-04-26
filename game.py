import pygame as pg
import sys
from core import settings
from typing import List
from objects import Object
from player import Player, Enemy
from tile import Cloud, TileMap


# class ObjectsInMemory:
#     def __init__(self, player, tilemap):
#         self.player = player
#         self.tilemap = tilemap
        
#     def update(self, display):
#         self.tilemap.update(display, self)
#         self.player.update(display, self)
        
#     @property
#     def all(self):
#         objects = [*self.tilemap.objects.values(), self.player]
#         return objects
    
#     def delete_objects(self):
#         # Remove objects from memory based on his atributes.
#         for obj in self.all:
#             pass
        
    # def update_player(self):
    #     self.player.update(self)
        
    # def update_tilemap(self):
    #     for tile in self.tilemap.tilemap_objects:
    #         tile.update(self)

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("ninja game")

        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        # It gives pixel art effect
        self.display = pg.Surface(
            (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT)
        )
        self.objs_in_memory: List[Object] = []
        self.clock = pg.time.Clock()
        self.tilemap = TileMap()
        self.objs_in_memory += self.tilemap.objects.values()
        # self.objs_in_memory = self.tilemap.tilemap_objects
            
    def run(self):
        # self.objs_in_memory.append(Cloud(100, 80))
        self.objs_in_memory.append(Player((80, 100), size=(16, 17)))
        
        while True:
            
            self.display.blit(self.tilemap.assets["sky"], (0, 0))
            # print("Quantidade de objetos na memória ", len(self.objs_in_memory))
            
            # self.generate_enemies()
            # self.tilemap.update(self.display, self.objects_update)
            
            self.objects_update()

            for event in pg.event.get():
                esc = pg.key.get_pressed()[pg.K_ESCAPE]
                if event.type == pg.QUIT or esc:
                    pg.quit()
                    sys.exit()
            
            self.screen.blit(
                pg.transform.scale(self.display, (self.screen.get_width(), self.screen.get_height()))
            )
            pg.display.update()
            self.clock.tick(60)
            
            
    def objects_update(self):
        for obj in self.objs_in_memory:
            obj.update(self.objs_in_memory, self.tilemap)
            obj.render(self.display)
            
            if not obj.can_delete:
                continue
            self.objs_in_memory.remove(obj)

        
    def generate_enemies(self):
        from random import randint
        num = randint(1, 50)
        if num != 2:
            return
        
        self.objs_in_memory.append(Enemy.generate(size=(25, 25)))
            
        
import pygame as pg
import slugs
from objects import StaticObject
from core.images import load_images
from core.mixins import LogCollisionMixin
from objects import StaticObject, Object
from typing import List

from random import randint
from time import sleep

# Maneira convencional
# [
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1],
# ]

NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class TileObject(LogCollisionMixin, StaticObject):
    slug = slugs.TILE
    

class TileMap:
    def __init__(self, tile_size=16):
        """
        # TileMap
        Usado para carregar mapas e gerar mapas para testes.
        
        ## Parameters
        - tile_size: 
        - tilemap: É mais vantajoso de trabalhar com física usando essa abordagem
        porque com a forma mais mais convencional, não teria muita liberdade
        de popular as partes em branco.
        Desenhos do 'objetos' baseado em sua localização no mapa e qual imagem
        será colocada no lugar. No data temos alguns mapas
        - offgrid_tiles: 'Objetos' que ficarão no espaço ao redor.
        
        
        """
        self.tile_size = tile_size
        self.tilemap = {} 
        self.offgrid_tiles = [] #
        self.assets = {
            "grass": load_images("tiles/grass/"),
            "stone": load_images("tiles/stone/"),
        }
        self.objects = {} # based on location
        
        self.generate_map()
        self.create_tile_objects()
        
    # def update(self, screen, objs):
    #     for tile_obj in self.objects:
    #         tile_obj.update(screen, objs)
        
    def tiles_around(self, pos):
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        # tile_loc_str = f"{tile_loc[0]};{tile_loc[1]}"
        tiles_around = []
        for offset in NEIGHBOUR_OFFSETS:
            location = f"{tile_loc[0] + offset[0]};{tile_loc[1] + offset[1]}"
            if not location in self.objects: # Exists neighborhoods
                continue
            tiles_around.append(self.objects[location])
            
        print(tiles_around)
        
        return tiles_around
            

    def create_tile_objects(self):
        for loc, tiles in self.tilemap.items():
            surface = self.assets[tiles["type"]][tiles["variant"]]
            position = (
                tiles["pos"][0] * self.tile_size, # without the * was going be inside others.
                tiles["pos"][1] * self.tile_size
            )
            
            # self.tilemap_objects.append(TileObject(position[0], position[1], surface))
            self.objects[loc] = TileObject(position[0], position[1], surface)

    
    def generate_map(self):
        for i in range(10):
            self.tilemap[f"{3 + i};10"] = {
                "type": "grass",
                "variant": 1,
                "pos": (3 + i, 10)
            }
        for i in range(10):
            self.tilemap[f"14;{10 + i}"] = {
                "type": "stone",
                "variant": 1,
                "pos": (14, 10 + i)
            }


def poison_player(instance, objs_in_memory, collisions):
    if not collisions:
        return 
    
    for obj in collisions:
        if obj.slug == "player":
            print("Player envenenado")
            obj.can_delete = True


class Cloud(StaticObject):
    frame_path = "clouds/cloud_1.png"
    # actions = [poison_player]
    slug = slugs.OFFGRID
    

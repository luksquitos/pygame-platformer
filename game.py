import pygame as pg
import sys
from typing import List
from objects import Object
from player import Player, Enemy
from tile import Cloud

objects_in_memory: List[Object] = []
class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("ninja game")
        self.screen = pg.display.set_mode((640, 480))
        self.clock = pg.time.Clock()
            
    def run(self):
        objects_in_memory.append(Player(x_pos=100, y_pos=200, size=(50, 50)))
        # objects_in_memory.append(Cloud(100, 80))
        
        while True:
            
            self.screen.fill((14, 219, 248)) # Usado para "limpar a tela"
            print("Quantidade de objetos na memória ", len(objects_in_memory))
            
            self.generate_enemies()
            
            self.objects_update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            pg.display.update()
            self.clock.tick(60)
            
            
    def objects_update(self):
        for obj in objects_in_memory:
            obj.update(self.screen, objects_in_memory)
            
            if not obj.can_delete:
                continue
            objects_in_memory.remove(obj)

        
    def generate_enemies(self):
        from random import randint
        num = randint(1, 50)
        if num != 2:
            return
        
        objects_in_memory.append(Enemy.generate(size=(50, 50)))
            
        
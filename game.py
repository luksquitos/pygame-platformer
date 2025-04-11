import pygame as pg
import sys
from player import Player, Enemy


class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("ninja game")
        self.screen = pg.display.set_mode((640, 480))
        self.clock = pg.time.Clock()
        self.player = Player(x_pos=100)
        self.enemies = []
            
    def run(self):
        while True:
            
            self.screen.fill((14, 219, 248)) # Usado para "limpar a tela"
            
            self.generate_enemies()
            print("quantidade de objetos", len(self.enemies))
            
            self.blit_objects()
            # self.screen.blit(
            #     self.player.frame, 
            #     (self.player.x_pos, self.player.y_pos)
            # ) # "Por outra 'surface' por cima"
            
            # self.player.update()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            pg.display.update()
            self.clock.tick(60)
            
            
    def blit_objects(self):
        self.screen.blit(
            self.player.frame,
            (self.player.x_pos, self.player.y_pos)
        )
        
        self.player.update()
        
        for obj in self.enemies:
            self.screen.blit(
                obj.frame, 
                (obj.x_pos, obj.y_pos)
            ) # "Por outra 'surface' por cima"
            obj.update()

        
    def generate_enemies(self):
        from random import randint
        num = randint(1, 30)
        if num != 2:
            return
        
        self.enemies.append(Enemy(x_pos=randint(100, 600)))
            
        
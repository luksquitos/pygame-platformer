import pygame as py
import sys

py.init()

py.display.set_caption("ninja game")
screen = py.display.set_mode((640, 640))

clock = py.time.Clock()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    
    py.display.update()
    clock.tick(60)
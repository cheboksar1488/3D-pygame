import pygame
from settings import *
from player import *
from map import *
from raycast import *


pygame.init()
clock=pygame.time.Clock()
player=Player()
MAP=Map()

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill(black)

    #MAP.draw_map()
    raycasting(player.posx, player.posy, player.angle)
    player.movement()
    #player.draw()

    pygame.display.flip()
    clock.tick(60)

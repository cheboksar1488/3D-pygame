import pygame, math, random

size=(1080, 720)
screen=pygame.display.set_mode(size)
half_height=size[1]//2

#map settings
Bsize=(100, 100)

#player settings
player_speed=2
player_rotate_speed=0.02
player_angle=0
player_position=(size[0]//2, size[1]//2)

#raycast settings
RANGE=500
rays=108
fov=math.pi//3
half_fov=fov/2
delta_angle=fov/rays
DIST=rays/(2*math.tan(half_fov))
proj_coef=DIST*Bsize[0]
SCALE=size[0]//rays


#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
gray=(125,125,125)

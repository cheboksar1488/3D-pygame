from settings import *
from map import walls_position
def raycasting(x, y, angle):
    first_ray=angle-half_fov
    for ray in range(rays):
        for distance in range(RANGE):
            xray=distance*math.sin(first_ray)+x
            yray=distance*math.cos(first_ray)+y
            if (xray//Bsize[0]*Bsize[1], yray//Bsize[0]*Bsize[1]) in walls_position:
                proj_height=proj_coef//distance
                pygame.draw.rect(screen, white, (ray*SCALE, half_height-proj_height//2, SCALE, proj_height))
        first_ray+=delta_angle
        
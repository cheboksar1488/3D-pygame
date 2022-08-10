from settings import *

map=[
    'wwwwwwwwwwww',
    'w........w.w',
    'wwww....w..w',
    'w.......w..w',
    'w.......wwww',
    'w....w.....w',
    'w....ww....w',
    'w..........w',
    'wwwwwwwwwwww',
]
walls_position=[]
for wy in range(len(map)):
    for wx in range(len(map[wy])):
        if map[wy][wx]=='w':
            position=(wx*Bsize[0], wy*Bsize[1])
            walls_position.append(position)
print(walls_position)   
class Map():
    def __init__(self):
        self.scale_map=5
        self.offset_x=0
        self.offset_y=0
    def draw_minimap(self):
        pass

    def draw_map(self):
        for x, y in walls_position:
            pygame.draw.rect(screen, white, (x, y, Bsize[0], Bsize[1]), 1)

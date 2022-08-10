from settings import *

class Player():
    def __init__(self):
        self.posx, self.posy=player_position
        self.angle=player_angle
    
    def movement(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.posx+=player_speed*math.sin(self.angle)
            self.posy+=player_speed*math.cos(self.angle)
        if key[pygame.K_s]:
            self.posx-=player_speed*math.sin(self.angle)
            self.posy-=player_speed*math.cos(self.angle)
        if key[pygame.K_d]:
            self.posx-=player_speed*math.cos(self.angle)
            self.posy+=player_speed*math.sin(self.angle)
        if key[pygame.K_a]:
            self.posx+=player_speed*math.cos(self.angle)
            self.posy-=player_speed*math.sin(self.angle)

        if key[pygame.K_RIGHT]:
            self.angle+=player_rotate_speed
        if key[pygame.K_LEFT]:
            self.angle-=player_rotate_speed
        
        self.linex=RANGE*math.sin(self.angle)+self.posx
        self.liney=RANGE*math.cos(self.angle)+self.posy

    def draw(self):
        pygame.draw.circle(screen, green, (self.posx, self.posy), 2)
        pygame.draw.aaline(screen, red, (self.posx, self.posy), (self.linex, self.liney))
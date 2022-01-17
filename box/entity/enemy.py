import pygame
import random
from config import width, height, enemy_bullet_speed, enemy_speed
from Bullet import Bullet
D = 10


class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy,armer):
        super().__init__() # ←この一行
        self.vx, self.vy = (vx, vy)
        self.image = pygame.Surface((D, D))
        self.image.fill((255,255,255))
        self.rect = pygame.Rect(x, y, D, D)
        self.MAXHP = armer
        self.armer = armer
        self.x = x
        self.y = y
        self.CDR = int(random.random()*30)+100
        self.counta = 0
    def update(self,x,y,e):
        if True != (0 < self.x < width-D-200):
            self.vx *= -1
        if True != (0< self.y < height-D):
            self.vy *= -1

        self.rect.move_ip(self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        self.shoot(x,y,e)
    def hit(self,e,h):
        self.armer -= 1
        if self.armer<=0:
            try:
                e.remove(h)
            except:
                pass
        elif self.armer == 2:
            self.image.fill((255,255,0))
        elif self.armer == 1:
            self.image.fill((255,0,0))
    def shoot(self,x,y,bullet):
        if self.CDR < self.counta:
            X = x - self.x
            Y = y - self.y
            time =  (X ** 2 + Y ** 2)**.5 / enemy_bullet_speed
            bullet.add(Bullet(self.x,self.y+D/2,X/time,Y/time,(255,0,0)))
            self.CDR = int(random.random()*30)+100
            self.ChangeSpeed()
            self.counta = 0
        else:
            self.counta += 1
    def ChangeSpeed(self):
        self.vx,self.vy = int(random.random() * enemy_speed - enemy_speed / 2), int(random.random() * enemy_speed - enemy_speed / 2)

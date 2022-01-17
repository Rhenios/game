import pygame
from Bullet import Bullet
from config import bulletspeed
from config import Tank_D, Tankspeed, tankcool as MD,Tankspeed,tankcool


class Tank(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy,armer):
        super().__init__()
        self.vx = vx
        self.vy = vy
        self.image = pygame.Surface((MD, MD))
        self.image.fill(((35, 255, 255)))
        self.rect = pygame.Rect(x, y, MD, MD)
        self.speed = Tankspeed
        self.x = x
        self.y = y
        self.cool = 0
        self.armer = armer

    def up(self):
        self.vy = -self.speed
    def down(self):
        self.vy = self.speed
    def right(self):
        self.vx = self.speed
    def left(self):
        self.vx = -self.speed

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy

        self.vx = 0
        self.vy = 0
        if self.cool <= 25:
            self.cool+= 1
        return self.x,self.y

    def shoot(self,bullets):
        if self.cooldown():
            bullets.add(Bullet(self.x,self.y+MD/2,-bulletspeed,0,(255,255,0)))
            bullets.add(Bullet(self.x, self.y + MD / 2, -bulletspeed, 1, (255, 255, 0)))
            bullets.add(Bullet(self.x, self.y + MD / 2, -bulletspeed, -1, (255, 255, 0)))
    def BIGshoot(self,bullets):
        bullets.add(Bullet(self.x,self.y+MD/2,-bulletspeed,0,(200,200,0),10))
    def cooldown(self):
        if self.cool >=tankcool:
            self.cool = 0
            return True
        else:
            return False

    def hit(self,e,h):
        self.armer -= 1
        if self.armer<=0:
            try:
                e.remove(h)
            except:
                pass
        elif self.armer <= self.armer//3*2:
            self.image.fill((255,255,0))
        elif self.armer <= self.armer//3:
            self.image.fill((0,0,255))
    def location(self):
        return self.x,self.y
    def Changespeed(self,v):
        self.speed = v
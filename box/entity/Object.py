import pygame
from config import D

class Object(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.armer = 100000000000
        self.image = pygame.Surface((D+5, D+5))
        self.image.fill((100,100,100))
        self.rect = pygame.Rect(x, y, D+5, D+5)

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
import pygame
from pygame.locals import *
import sys
from box.sys.button import Button


class opening:
    def __init__(self, w, h, FPS):
        pygame.init()
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("シューティングRPG")
        self.clock = pygame.time.Clock()
        self.h = h
        self.w = w
        self.FPS = FPS
        self.key = True
        self.ping = 0
    def animation(self):
        while self.key:
            self.screen.fill((0,0,0))
            button = Button((self.w/2-100,self.h/2-200),50,10,(255,255,255),(0,0,0),"Hello world")
            button.draw(self.screen)
            button.update()
            button = Button((self.w/2,self.h/2),30,10,(255,255,255),(0,0,0),"Hello world")
            button.update()
            button.draw(self.screen)
            button = Button((self.w/2,self.h/2+100),30,10,(255,255,255),(0,0,0),"Hello world")
            button.update()
            button.draw(self.screen)
            button = Button((self.w/2,self.h/2+200),30,10,(255,255,255),(0,0,0),"hello")
            button.update("exit")
            button.draw(self.screen)
            print(self.ping)
            self.ping += 1
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    key = False
                elif event.type == pygame.K_ESCAPE:
                    key = False
        pygame.quit()
        sys.exit()


from box.entity.MyTank import Tank
from box.entity.enemy import enemy as Target
from ..config import enemy_speed as enemyspeed
from ..config import base_count

import pygame
import random

class battle():

    def __init__(self,w,h,enemyc,FPS,ObjectLevel):
        self.screen = pygame.display.set_mode((w,h))
        self.clock = pygame.time.Clock()
        self.h = h
        self.w = w
        self.FPS = FPS
        self.enemys = pygame.sprite.Group()
        for i in range(enemyc):
            self.addenemy()
        self.tank = pygame.sprite.GroupSingle()
        self.tank.add(Tank(1180,360,0,0,1))
        self.bullets = pygame.sprite.Group()
        self.ebullets = pygame.sprite.Group()
        self.x,self.y = 0,0
        self.objects = pygame.sprite.Group()
        self.Big_shoot_key = True
        for i in range(base_count*ObjectLevel):
            self.addobject()

    def addenemy(self):
        self.enemys.add(Target(int(random.random() * (self.w - 500)), int(random.random() * (self.h - 100) + 50),
                              int(random.random() * enemyspeed - enemyspeed / 2), int(random.random() * enemyspeed - enemyspeed / 2), 3))

    def animation(self,screen):
        self.done = True
        while self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.done = False
            if self.enemys == None:self.done = False
            self.clock.tick(self.FPS)
            pressed_keys = pygame.key.get_pressed()
            for tk in self.tank:
                if pressed_keys[pygame.K_UP]:
                    tk.up()
                if pressed_keys[pygame.K_DOWN]:
                    tk.down()
                if pressed_keys[pygame.K_RIGHT]:
                    tk.right()
                if pressed_keys[pygame.K_LEFT]:
                    tk.left()
                if pressed_keys[pygame.K_SPACE]:
                    tk.shoot(self.bullets)
                if pressed_keys[pygame.K_d]:
                    print(self.Big_shoot_key)
                    if self.Big_shoot_key:
                        self.Big_shoot_key = False
                        tk.BIGshoot(self.bullets)
                else:
                    self.Big_shoot_key= True
                self.x,self.y = tk.location()
            if pressed_keys[pygame.K_ESCAPE]:
                self.done = False
            self.tank.update()
            self.bullets.update()
            self.ebullets.update()
            self.enemys.update(self.x,self.y,self.ebullets)
            collided_E_B = pygame.sprite.groupcollide(self.enemys, self.bullets, False, True)
            for hit in collided_E_B:
                hit.hit(self.enemys, hit)
            cokkided = pygame.sprite.groupcollide(self.tank,self.ebullets,False,True)
            for hit in cokkided:
                hit.hit(self.tank,hit)
            cokkided = pygame.sprite.groupcollide(self.tank,self.objects,False,False)
            for hit in cokkided:
                hit.Changespeed(0)
            cokkided = pygame.sprite.groupcollide(self.objects,self.ebullets,False,True)
            cokkided = pygame.sprite.groupcollide(self.objects, self.bullets, False, True)
            self.ebullets.draw(screen)
            self.tank.draw(screen)
            self.enemys.draw(screen)
            self.bullets.draw(screen)
            self.objects.draw(screen)
            pygame.display.flip()
            screen.fill((0, 0, 0))
        pygame.quit()


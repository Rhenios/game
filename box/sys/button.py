import sys

import pygame
from pygame.rect import Rect


class Button:
    def __init__(self, pos, size, pad, color, txtcolor, text="Button"):
        self.x = pos[0]
        self.y = pos[1]
        self.pad = pad
        self.color = color
        self.font = pygame.font.SysFont(None, size)
        self.text = self.font.render(text, True, txtcolor)
        self.button = Rect(pos, (self.text.get_width() + pad, self.text.get_height() + pad))
        self.button_bottom = Rect(pos, (self.button.width, self.button.height + 5))

    def update(self,commands="None"):
        self.button.top = self.y

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.button.top += 2
                    print(u"ボタンが押されました")
                    if commands == "exit":
                        self.exit()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(self.text, (self.x + self.pad / 2, self.y + self.pad / 2))

    def exit(self):
        pygame.quit()
        sys.exit()
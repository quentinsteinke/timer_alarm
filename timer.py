import pygame
import time


class Timer:
    white = (255, 255, 255)

    def __init__(self, font="script", size=32, color=white, text="text"):
        self.text = text
        self.size = size
        self.font = font
        self.color = color

        self.object = pygame.font.Font(self.font, self.size)
    

    def draw(self):
        self.object.render(self.text, True, self.color)

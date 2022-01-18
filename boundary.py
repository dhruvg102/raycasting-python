import sys, pygame

pygame.init()

class Wall:
    def __init__(self, a, b, screen):
        self.a = a
        self.b = b
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, (255, 255, 255), self.a, self.b)

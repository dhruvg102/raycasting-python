import pygame, math
import ray
from ray import Ray

pygame.init()

class Particle:
    def __init__(self, pos, screen, a):
            self.pos = pos
            self.rays = []
            self.screen = screen
            self.a = a
            i = 0
            while i < 288:
                self.rays.append(Ray(self.pos, i / 4 + self.a, self.screen))
                i += 1

    # def update(self):
    #     self.pos = pygame.mouse.get_pos()

    def show(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.pos, 5)
        for r in self.rays:
            r.show()
            #r.lookAt()

    def look(self, walls):
        scene = []
        for r in self.rays:
            closest = None
            record = math.inf
            for wall in walls:
                pt = r.cast(wall)
                if pt:
                    d = math.dist(self.pos, pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest:
                pygame.draw.line(self.screen, (200, 200, 200), self.pos, closest)
            scene.append(record)
        return scene

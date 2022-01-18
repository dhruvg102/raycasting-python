import pygame, sys, random, math
from perlin_noise import PerlinNoise
import boundary
import ray
import particle
from boundary import Wall
from ray import Ray
from particle import Particle

screenW = 1200
screenH = 600
xoff = 10
yoff = 100000
noise = PerlinNoise()
view = 0

def remap(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


pygame.init()


def rect(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


screen = pygame.display.set_mode((screenW, screenH))
screen.fill((45,45,45))
i = 0
walls = []
walls.append(Wall((0,0), (0,600), screen))
walls.append(Wall((0,0), (600,0), screen))
walls.append(Wall((600,600), (0,600), screen))
walls.append(Wall((600,600), (599,0), screen))
while i < 4:
    walls.append(Wall((random.randint(1, screenW/2), random.randint(1, screenH)), (random.randint(1, screenW/2), random.randint(1, screenH)), screen))
    i += 1
# ray = Ray((200,200), 0, screen)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        view -= 0.2
    if keys[pygame.K_RIGHT]:
        view += 0.2


    screen.fill((50,50,50))
    #particle = Particle((noise(xoff) * screenW/2 + 300, noise(yoff) * screenH + 300), screen)
    particle = Particle(pygame.mouse.get_pos(), screen, view  % 360)

    for wall in walls:
        wall.show()
    particle.show()
    # xoff += 0.0005
    # yoff += 0.0005





    scene = particle.look(walls)
    #print(scene)
    w = screenW/(2 * len(scene))
    i = 0
    while i < len(scene):

        if scene[i] == math.inf:
            fill = screenW/2
        else:
            fill = math.floor(scene[i])
            # if fill > 255:
            #     fill = 255

        alpha = remap(fill, 0, screenW/2, 255, 0)
        h = remap(fill, 0, screenW/2, screenH, 0)
        wallrect = pygame.Rect(screenW/2 + i * w, 0, w + 2, h)
        wallrect.center = (screenW/2 + i * w, screenH/2)
        rect(screen, (255, 255, 255, alpha), wallrect)
        i +=1





    # ray.show()
    # ray.lookAt()
    # pt = ray.cast(wall)
    # if pt:
    #    pygame.draw.circle(screen, (0,0,255), pt, 5)

    pygame.display.update();

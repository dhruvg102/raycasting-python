import pygame, math

pygame.init()

def coord(pos, angle):
    newposx = 1 * math.cos(math.radians(angle)) + pos[0]
    newposy = 1 * math.sin(math.radians(angle)) + pos[1]
    newpos = [newposx, newposy]
    return newpos

def calcangle(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    den =  (x2 - x1)
    if den == 0:
        return 0
    else:
        return math.degrees(math.atan((y2 - y1)/den))

class Ray:
    def __init__(self, pos, angle, screen):
        self.pos = pos
        self.angle = angle
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, (255, 255, 255), self.pos, coord(self.pos, self.angle))

    def lookAt(self):
        self.angle += calcangle(self.pos, pygame.mouse.get_pos())

    def cast(self, wall):
        x1 = wall.a[0]
        y1= wall.a[1]
        x2 = wall.b[0]
        y2 = wall.b[1]

        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = coord(self.pos, self.angle)[0]
        y4 = coord(self.pos, self.angle)[1]


        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return

        #return (x1,y1,x2,y2,x3,y3,x4,y4)

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den


        if 0 < t and t < 1 and u > 0:
            ptx = x1 + t * (x2 - x1)
            pty = y1 + t * (y2 - y1)
            pt = [ptx, pty]
            return pt
        else:
            return

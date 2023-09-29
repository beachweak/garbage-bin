import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math  # we missed this line 

SCREEN_SIZE = (1920, 1080)
SCALAR = .5
SCALAR2 = 0.2

def Torus():
    glBegin(GL_QUAD_STRIP)
    for i in range(21):
        for j in range(21):
            glVertex3f(SCALAR*math.cos((math.pi/5)*i)*math.cos((math.pi/5)*j), SCALAR*math.sin((math.pi/5)*i)*math.cos((math.pi/5)*j), SCALAR*math.sin((math.pi/5)*j))
            glVertex3f(SCALAR*math.cos((math.pi/5)*(i+1))*math.cos((math.pi/5)*j), SCALAR*math.sin((math.pi/5)*(i+1))*math.cos((math.pi/5)*j), SCALAR*math.sin((math.pi/5)*j))
            glVertex3f(SCALAR*math.cos((math.pi/5)*(i+1))*math.cos((math.pi/5)*(j+1)), SCALAR*math.sin((math.pi/5)*(i+1))*math.cos((math.pi/5)*(j+1)), SCALAR*math.sin((math.pi/5)*(j+1)))
            glVertex3f(SCALAR*math.cos((math.pi/5)*i)*math.cos((math.pi/5)*(j+1)), SCALAR*math.sin((math.pi/5)*i)*math.cos((math.pi/5)*(j+1)), SCALAR*math.sin((math.pi/5)*(j+1)))
    glEnd()

def main():
    pygame.init()
    display = (SCREEN_SIZE)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Torus()
        pygame.display.flip()
        pygame.time.wait(10)


main()
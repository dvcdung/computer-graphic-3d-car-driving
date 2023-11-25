import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pyrr

class UFO(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, z = 0, x_rotate = 0, y_rotate = 0, z_rotate = 0):
        super().__init__()

        self.x = x
        self.y = y
        self.z = z
        self.x_rotate = x_rotate
        self.y_rotate = y_rotate
        self.z_rotate = z_rotate
        self.speed = [30, 30, 50]
        self.bound = {"x": 0.15, "y": 0.075, "z": 0.15}


    def update(self):
        self.draw_ufo()

    def draw_ufo(self):
        # Bottom
        glBegin(GL_QUADS)
        glColor(0.25, 0.25, 0.25)
        glVertex3f(self.x - 0.075, self.y -0.1, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y -0.1, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y -0.1, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y -0.1, self.z + 0.075)
        glEnd()
        # Arround - B
        glBegin(GL_QUADS)
        glColor(0.35, 0.35, 0.35)
        glVertex3f(self.x - 0.075, self.y -0.1, self.z - 0.075)
        glVertex3f(self.x - 0.075, self.y -0.02, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y -0.02, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y -0.1, self.z - 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.35, 0.35, 0.35)
        glVertex3f(self.x + 0.075, self.y -0.1, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y -0.02, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y -0.02, self.z + 0.075)
        glVertex3f(self.x + 0.075, self.y -0.1, self.z + 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.35, 0.35, 0.35)
        glVertex3f(self.x - 0.075, self.y -0.1, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y -0.02, self.z + 0.075)
        glVertex3f(self.x + 0.075, self.y -0.02, self.z + 0.075)
        glVertex3f(self.x + 0.075, self.y -0.1, self.z + 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.35, 0.35, 0.35)
        glVertex3f(self.x - 0.075, self.y -0.1, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y -0.02, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y -0.02, self.z - 0.075)
        glVertex3f(self.x - 0.075, self.y -0.1, self.z - 0.075)
        glEnd()

        # Bottom - M
        glBegin(GL_QUADS)
        glColor(0.4, 0.4, 0.4)
        glVertex3f(self.x - 0.15, self.y -0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y -0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y -0.02, self.z + 0.15)
        glVertex3f(self.x - 0.15, self.y -0.02, self.z + 0.15)
        glEnd()

        # Arround - M
        glBegin(GL_QUADS)
        glColor(0.5, 0.5, 0.5)
        glVertex3f(self.x - 0.15, self.y -0.02, self.z - 0.15)
        glVertex3f(self.x - 0.15, self.y +0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y +0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y -0.02, self.z - 0.15)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.5, 0.5, 0.5)
        glVertex3f(self.x + 0.15, self.y -0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y +0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y +0.02, self.z + 0.15)
        glVertex3f(self.x + 0.15, self.y -0.02, self.z + 0.15)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.5, 0.5, 0.5)
        glVertex3f(self.x - 0.15, self.y -0.02, self.z + 0.15)
        glVertex3f(self.x - 0.15, self.y +0.02, self.z + 0.15)
        glVertex3f(self.x + 0.15, self.y +0.02, self.z + 0.15)
        glVertex3f(self.x + 0.15, self.y -0.02, self.z + 0.15)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.5, 0.5, 0.5)
        glVertex3f(self.x - 0.15, self.y -0.02, self.z + 0.15)
        glVertex3f(self.x - 0.15, self.y +0.02, self.z + 0.15)
        glVertex3f(self.x - 0.15, self.y +0.02, self.z - 0.15)
        glVertex3f(self.x - 0.15, self.y -0.02, self.z - 0.15)
        glEnd()
  
        # Top - M
        glBegin(GL_QUADS)
        glColor(0.6, 0.6, 0.6)
        glVertex3f(self.x - 0.15, self.y +0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y +0.02, self.z - 0.15)
        glVertex3f(self.x + 0.15, self.y +0.02, self.z + 0.15)
        glVertex3f(self.x - 0.15, self.y +0.02, self.z + 0.15)
        glEnd()
        
        # Arround - T
        glBegin(GL_QUADS)
        glColor(0.65, 0.65, 0.65)
        glVertex3f(self.x - 0.075, self.y +0.1, self.z - 0.075)
        glVertex3f(self.x - 0.075, self.y +0.09, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.09, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.1, self.z - 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.65, 0.65, 0.65)
        glVertex3f(self.x - 0.075, self.y +0.03, self.z - 0.075)
        glVertex3f(self.x - 0.075, self.y +0.02, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.02, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.03, self.z - 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.65, 0.65, 0.65)
        glVertex3f(self.x - 0.075, self.y +0.09, self.z - 0.075)
        glVertex3f(self.x - 0.065, self.y +0.09, self.z - 0.075)
        glVertex3f(self.x - 0.065, self.y +0.03, self.z - 0.075)
        glVertex3f(self.x - 0.075, self.y +0.03, self.z - 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.65, 0.65, 0.65)
        glVertex3f(self.x + 0.075, self.y +0.09, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.03, self.z - 0.075)
        glVertex3f(self.x + 0.065, self.y +0.03, self.z - 0.075)
        glVertex3f(self.x + 0.065, self.y +0.09, self.z - 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.62, 0.62, 0.62)
        glVertex3f(self.x + 0.075, self.y +0.1, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.02, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.02, self.z + 0.075)
        glVertex3f(self.x + 0.075, self.y +0.1, self.z + 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.65, 0.65, 0.65)
        glVertex3f(self.x - 0.075, self.y +0.1, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y +0.02, self.z + 0.075)
        glVertex3f(self.x + 0.075, self.y +0.02, self.z + 0.075)
        glVertex3f(self.x + 0.075, self.y +0.1, self.z + 0.075)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0.62, 0.62, 0.62)
        glVertex3f(self.x - 0.075, self.y +0.1, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y +0.02, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y +0.02, self.z - 0.075)
        glVertex3f(self.x - 0.075, self.y +0.1, self.z - 0.075)
        glEnd()
        # Top
        glBegin(GL_QUADS)
        glColor(0.7, 0.7, 0.7)
        glVertex3f(self.x - 0.075, self.y +0.1, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.1, self.z - 0.075)
        glVertex3f(self.x + 0.075, self.y +0.1, self.z + 0.075)
        glVertex3f(self.x - 0.075, self.y +0.1, self.z + 0.075)
        glEnd()

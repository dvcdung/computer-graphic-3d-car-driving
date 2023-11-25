import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import pyrr

class Meteorite(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, z = 0, x_rotate = 0, y_rotate = 0, z_rotate = 0):
        super().__init__()

        self.x = x
        self.y = y
        self.z = z
        self.x_rotate = x_rotate
        self.y_rotate = y_rotate
        self.z_rotate = z_rotate
        self.color = (random.uniform(0.2, 1.0), random.uniform(0.2, 1.0), random.uniform(0.2, 1.0))
        self.random_num = random.randint(8, 25)
        self.radius = random.uniform(0.025, random.uniform(0.03, random.uniform(0.035, random.uniform(0.04, 1.25))))
        self.bound = {"x": 0.15, "y": 0.075, "z": 0.15}


    def update(self):
        glPushMatrix()
        glRotatef(self.x_rotate, 1, 0, 0)
        glRotatef(self.y_rotate, 0, 1, 0)
        glRotatef(self.z_rotate, 0, 0, 1)
        self.draw_mateorite()
        glPopMatrix()

    def draw_mateorite(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        quadric = gluNewQuadric()
        glColor(self.color[0], self.color[1], self.color[2])
        gluSphere(quadric, self.radius, self.random_num, self.random_num)
        gluDeleteQuadric(quadric)
        glPopMatrix()

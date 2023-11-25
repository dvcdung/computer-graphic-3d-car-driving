import pygame
from pygame.locals import *
from game.components.ufo import UFO
from game.components.meteorite import Meteorite

class GameManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_over = False
        self.clock = pygame.time.Clock()

        self.x_rotate = 0
        self.y_rotate = 0 
        self.z_rotate = 0
        self.x_translate = 0
        self.y_translate = 0
        self.z_translate = 0
        self.move_unit = 0.01
        self.rotate_unit = 0.02
        
        self.ufo = UFO (self.x_translate, self.y_translate, self.z_translate, self.x_rotate, self.y_rotate, self.z_rotate)
        self.meteorite = Meteorite(1, 1, -10, 0, 0, 0)

    def handle_events(self):
            # Điều khiển camera với các phím mũi tên và các phím số
            keys = pygame.key.get_pressed()
            if keys[K_a]:
                if self.z_rotate < 1:
                    if self.z_rotate > 1:
                        self.z_rotate = 1
                        pass
                    self.z_rotate += self.rotate_unit
            if keys[K_d]:
                if self.z_rotate > -1:
                    if self.z_rotate < -1:
                        self.z_rotate = -1
                        pass
                    self.z_rotate -= self.rotate_unit
            if not keys[K_a] and not keys[K_d] and self.z_rotate != 0:
                    i = self.z_rotate/abs(self.z_rotate)
                    if int(self.z_rotate/self.rotate_unit*5) == 0:
                        self.z_rotate = 0
                        pass
                    self.z_rotate = (abs(self.z_rotate) - self.rotate_unit)*i

            if keys[K_UP]:
                if self.x_rotate > -1:
                    if self.x_rotate < -1:
                        self.x_rotate = -1
                        pass
                    self.x_rotate -= self.rotate_unit
            if keys[K_DOWN]:
                if self.x_rotate < 1:
                    if self.x_rotate > 1:
                        self.x_rotate = 1
                        pass
                    self.x_rotate += self.rotate_unit
            if not keys[K_UP] and not keys[K_DOWN] and self.x_rotate != 0:
                    i = self.x_rotate/abs(self.x_rotate)
                    if int(self.x_rotate/self.rotate_unit*5) == 0:
                        self.x_rotate = 0
                        pass
                    self.x_rotate = (abs(self.x_rotate) - self.rotate_unit)*i

            if keys[K_LEFT]:
                if self.y_rotate > -1:
                    if self.y_rotate < -1:
                        self.y_rotate = -1
                        pass
                    self.y_rotate -= self.rotate_unit
            if keys[K_RIGHT]:
                if self.y_rotate < 1:
                    if self.y_rotate > 1:
                        self.y_rotate = 1
                        pass
                    self.y_rotate += self.rotate_unit
            if not keys[K_LEFT] and not keys[K_RIGHT] and self.y_rotate != 0:
                    i = self.y_rotate/abs(self.y_rotate)
                    if int(self.y_rotate/self.rotate_unit*5) == 0:
                        self.y_rotate = 0
                        pass
                    self.y_rotate = (abs(self.y_rotate) - self.rotate_unit)*i
                    
            if keys[K_w]:
                if self.z_translate < 1:
                    if self.y_rotate > 1:
                        self.y_rotate = 1
                        pass
                    self.z_translate += self.move_unit
            elif not keys[K_SPACE]:
                if self.z_translate > 0.0:
                    self.z_translate -= self.move_unit*2
                    if self.z_translate < 0.0: self.z_translate = 0.0
            if keys[K_SPACE]:
                if self.z_translate > 0.0:
                    self.z_translate -= self.move_unit
                    if self.z_translate < 0.0: self.z_translate = 0.0

    def update(self):
        self.meteorite.update()
        self.meteorite.x -= self.ufo.speed[0]*self.x_translate*0.002
        self.meteorite.y -= self.ufo.speed[1]*self.y_translate*0.002
        self.meteorite.z += self.ufo.speed[2]*self.z_translate*0.002
        self.meteorite.x_rotate += self.x_rotate*0.5
        self.meteorite.y_rotate += self.y_rotate
        self.meteorite.z_rotate += self.z_rotate*0.5
        self.ufo.update()
        # self.ufo.x += self.ufo.speed[0]*self.x_translate
        # self.ufo.y += self.ufo.speed[1]*self.y_translate
        # self.ufo.z -= self.ufo.speed[2]*self.z_translate
        self.ufo.x_rotate += self.x_rotate
        self.ufo.y_rotate += self.y_rotate
        self.ufo.z_rotate += self.z_rotate
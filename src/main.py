import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game.game_manager import GameManager
import pyrr

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ game
width, height = 1600, 900
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("UFO")

# Khởi tạo camera
glMatrixMode(GL_PROJECTION)
projection_matrix = pyrr.matrix44.create_perspective_projection_matrix(45, width/height, 0.1, 50.0)
glLoadMatrixf(projection_matrix)
glMatrixMode(GL_MODELVIEW)
a = -0.1
b = -2
status = 0
glTranslatef(0.0, -0.055, -0.03)

# Tạo đối tượng GameManager
game_manager = GameManager(width, height)

# Chạy game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Thay đổi góc nhìn
    # glRotatef(game_manager.y_rotate, 0, 1, 0)
    # glRotatef(game_manager.x_rotate, 1, 0, 0)
    # glRotatef(game_manager.z_rotate, 0, 0, 1)

    # Di chuyển camera theo trục Z
    # glTranslatef(0.0, 0.0, -game_manager.z_translate)

    # Xử lý sự kiện và cập nhật trạng thái game
    game_manager.handle_events()
    game_manager.update()

    pygame.display.flip()
    pygame.time.wait(10)

import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = [5, 5]

    def update(self):
        self.rect.move_ip(self.speed)

    def bounce(self):
        self.speed[1] = -self.speed[1]

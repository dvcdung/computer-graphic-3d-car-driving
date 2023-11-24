import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.move_ip(self.speed, 0)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.rect.right < 800:
            self.rect.move_ip(self.speed, 0)

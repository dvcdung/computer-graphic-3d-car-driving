import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass  # Đối tượng đường không cần cập nhật nên hàm update rỗng

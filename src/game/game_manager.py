import pygame
from game.ball import Ball
from game.paddle import Paddle
from game.road import Road

class GameManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_over = False
        self.clock = pygame.time.Clock()

        # Tạo đối tượng viên bi và thanh điều khiển
        self.ball = Ball(width // 2, height // 2)
        self.paddle = Paddle(width // 2 - 50, height - 20)
        
        # Tạo đối tượng Road
        road_width = 400
        road_height = 20
        road_color = (128, 128, 128)  # Màu xám
        self.road = Road((width - road_width) // 2, height - road_height, road_width, road_height, road_color)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()

    def update(self):
        # Cập nhật trạng thái viên bi và thanh điều khiển
        self.ball.update()
        self.paddle.update()

        # Kiểm tra va chạm giữa viên bi và thanh điều khiển
        if pygame.sprite.collide_rect(self.ball, self.paddle):
            self.ball.bounce()

        # Kiểm tra va chạm với biên trên và dưới
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.height:
            self.ball.bounce()

        # Kiểm tra va chạm với đối tượng Road
        if pygame.sprite.collide_rect(self.ball, self.road):
            self.ball.bounce()

        # Kiểm tra game over
        if self.ball.rect.top > self.height:
            self.game_over = True

    def draw(self, screen):
        # Vẽ viên bi và thanh điều khiển lên màn hình
        screen.fill((255, 255, 255))
        screen.blit(self.ball.image, self.ball.rect)
        screen.blit(self.paddle.image, self.paddle.rect)

        # Vẽ đối tượng Road lên màn hình
        screen.blit(self.road.image, self.road.rect)

        # Vẽ biên của cửa sổ game
        pygame.draw.line(screen, (0, 0, 0), (0, self.height - 1), (self.width, self.height - 1), 2)

        # Hiển thị điểm số (có thể thêm vào nếu muốn)

        # Giới hạn tốc độ frame
        self.clock.tick(60)
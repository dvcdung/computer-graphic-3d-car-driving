import pygame
from game.game_manager import GameManager

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bắn viên bi")

# Tạo đối tượng GameManager
game_manager = GameManager(width, height)

# Chạy game
while not game_manager.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_manager.game_over = True

    # Xử lý sự kiện và cập nhật trạng thái game
    game_manager.handle_events()
    game_manager.update()

    # Vẽ đối tượng lên màn hình
    game_manager.draw(screen)

    # Cập nhật màn hình
    pygame.display.update()

# Kết thúc game
pygame.quit()

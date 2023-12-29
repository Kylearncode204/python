import pygame
import sys

pygame.init()

# Tạo cửa sổ game
pygame.display.set_caption('game lon')
icon = pygame.image.load(r'image/5a371a5a34df47.5239089615135606662166.png')
pygame.display.set_icon(icon)

# Thêm hình nền
bak = pygame.image.load(r'FileGame/assets/background-night.png')

screen = pygame.display.set_mode((432, 768))

# Vòng lặp xử lí game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ hình nền
    screen.blit(bak, (0, 100))

    # Cập nhật màn hình
    pygame.display.update()

pygame.quit()
sys.exit()

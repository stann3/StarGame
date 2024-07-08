import pygame
import random
import sys
from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet

# Инициализиране на Pygame
pygame.init()

# Първоначално създаване на прозореца
screen = pygame.display.set_mode((screen_width, screen_height))

# Заглавие на прозореца
pygame.display.set_caption("2D Шутър Игра")

# Шрифт за точките
font = pygame.font.SysFont("Arial", 30)

# Флаг за цял екран
fullscreen = False

# Създаване на групи за спрайтовете
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Създаване на играча
player = Player()
all_sprites.add(player)

# Създаване на враговете
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Първоначални точки
score = 0

# Основен цикъл на играта
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            if event.key == pygame.K_f:  # Превключване на цял екран с 'F'
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    screen_width, screen_height = screen.get_size()
                else:
                    screen = pygame.display.set_mode((800, 600))
                    screen_width, screen_height = 800, 600
                player.rect.x = screen_width // 2
                player.rect.y = screen_height - player.rect.height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop_x()
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.stop_y()

    # Обновяване на всички спрайтове
    all_sprites.update()

    # Проверка за сблъсъци между куршуми и врагове
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 10  # Добавяне на точки при унищожаване на враг
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Проверка за сблъсъци между играча и враговете
    if pygame.sprite.spritecollideany(player, enemies):
        running = False

    # Рисуване на всички спрайтове
    screen.fill(black)
    all_sprites.draw(screen)

    # Рисуване на точките
    score_text = font.render(f"Точки: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # Обновяване на екрана
    pygame.display.flip()

    # Настройка на FPS
    clock.tick(60)

pygame.quit()
sys.exit()

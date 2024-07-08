import pygame
from settings import screen_width, screen_height, blue

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.change_x = 0
        self.change_y = 0
        self.gravity = 0.5

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0

        self.change_y += self.gravity

    def move_left(self):
        self.change_x = -6

    def move_right(self):
        self.change_x = 6

    def move_up(self):
        self.change_y = -6

    def move_down(self):
        self.change_y = 6

    def stop_x(self):
        self.change_x = 0

    def stop_y(self):
        self.change_y = 0

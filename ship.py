import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('Code/spaceship.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    

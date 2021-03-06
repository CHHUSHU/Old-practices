import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    
    bg_color = (230, 230, 230)
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        
        pygame.display.flip()

run_game()


import pygame, os, ctypes

from pygame.sprite import Group
from sheep import Sheep
from settings import Settings
from game_stats import GameStats
import game_functions as gf

def run_game():
    # Inicializa pygame, screen, e settings.
    pygame.init()
    pygame.display.set_caption("Black Sheep")

    user32 = ctypes.windll.user32
    screenSize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    screen = pygame.display.set_mode((screenSize), pygame.FULLSCREEN)

    settings = Settings(screenSize)

    # Cria uma instância do GameStats para armazenas as estatísticas do jogo.
    stats = GameStats()

    # Inicia a ovelha preta.
    black_sheep = Sheep(screen, settings, "black")

    while True:
        # Verifica evento do Mouse e Teclado.
        gf.check_keydown_events(stats, black_sheep)

        # Carrega o menu
        if stats.game_active == "menu":
            black_sheep = Sheep(screen, settings, "black")
            font = pygame.font.SysFont(None, 128)
            title = font.render('Black Sheep', True, settings.font_color)

            screen.fill(settings.bg_color)
            screen.blit(title, [screen.get_rect().right - (title.get_size()[0] + screenSize[0] / 20),
                                screen.get_rect().centery / 2 - (title.get_size()[1] / 2)])

            gf.button(screen, settings, stats, screenSize)

        # Movimenta as ovelhas.
        elif stats.game_active == "move":
            black_sheep.update(settings)

            screen.fill(settings.bg_color)            
            black_sheep.blitme()
            
            gf.check_click(pygame.mouse.get_pos(), stats, black_sheep)

        # Redesenha a tela.
        pygame.display.flip()


run_game()

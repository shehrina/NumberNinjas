import pygame
from MainGamePage import gamePage
from progress import progress_main
from OpeneingScreen import main_menu
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (150, 150, 150)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Ninjas")

title_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)


def draw_text(text, font, color, surface, x, y, underline=False):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)
    if underline:
        underline_rect = pygame.Rect(text_rect.left, text_rect.bottom - 5, text_rect.width, 3)
        pygame.draw.rect(surface, color, underline_rect)


def user_menu(user):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background_image = pygame.image.load('assets/background.jpg')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    gamePage(user)
                elif player_stats_button_rect.collidepoint(mouse_pos):
                    progress_main(user)
                elif back_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        draw_text("Welcome to Number Ninjas", title_font, BLACK, screen, WIDTH // 2, 80, underline=True)

        button_width = 200
        button_height = 50
        button_margin = 20
        x = WIDTH // 2
        y = 200  # Adjusted the y position to position buttons higher

        play_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, play_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, play_button_rect)
        draw_text("Play", button_font, BLACK, screen, x, y + button_height // 2)

        y += button_height + button_margin
        player_stats_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, player_stats_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, player_stats_button_rect)
        draw_text("Player Stats", button_font, BLACK, screen, x, y + button_height // 2)

        y += button_height + button_margin
        back_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, back_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, back_button_rect)
        draw_text("Exit Game", button_font, BLACK, screen, x, y + button_height // 2)

        pygame.display.flip()


if __name__ == "__main__":
    main_menu(super)

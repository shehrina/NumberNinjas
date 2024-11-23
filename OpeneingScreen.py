import pygame
import sys
pygame.init()


WIDTH, HEIGHT = 800, 600
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (150, 150, 150)
DARK_RED = (139, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Ninjas")

title_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)


def draw_text(text, font, color, surface, x, y, underline=False):
    """
    Draws text onto the game screen.

    🖌️ Parameters:
    - text (str): The message to display.
    - font (pygame.font.Font): The font style of the text.
    - color (tuple): The color of the text in RGB format.
    - surface (pygame.Surface): The pygame surface on which to draw.
    - x (int): The x-coordinate for the text placement.
    - y (int): The y-coordinate for the text placement.
    - underline (bool, optional): If True, underlines the text. Defaults to False.
    """
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)
    if underline:
        underline_rect = pygame.Rect(text_rect.left, text_rect.bottom - 5, text_rect.width, 3)
        pygame.draw.rect(surface, color, underline_rect)


def main_menu(screen, title_font, button_font, WHITE, BLACK, LIGHT_GRAY, WIDTH, HEIGHT):
    """
    Displays the main menu of the Number Ninjas game.

    🎮 Parameters:
    - screen (pygame.Surface): The main game screen to display elements.
    - title_font (pygame.font.Font): Font for the game title.
    - button_font (pygame.font.Font): Font for menu buttons.
    - WHITE, BLACK, LIGHT_GRAY (tuple): RGB color codes.
    - WIDTH, HEIGHT (int): Dimensions of the game screen.

    🚀 Launches the player into the heart of Number Ninjas, where adventure begins!
    Dive into a dojo of digits and equations by choosing your path right from the start.
    """
    background_image = pygame.image.load('assets/background.jpg')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    credit_font = pygame.font.Font(None, 24)
    while True:
        screen.blit(background_image, (0, 0)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if login_button_rect.collidepoint(mouse_pos):
                    print("Login Button Clicked")
                    return 'signin'
                elif signup_button_rect.collidepoint(mouse_pos):
                    print("Signup Button Clicked")
                    return 'signup'
                elif scoreboard_button_rect.collidepoint(mouse_pos):
                    print("Scoreboard Button Clicked")
                    return 'scoreboard'
                elif tutorial_button_rect.collidepoint(mouse_pos):
                    print("Tutorial Button Clicked")
                    return 'tutorial'
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        draw_text("Welcome to Number Ninjas", title_font, DARK_RED, screen, WIDTH // 2, 80, underline=True)

        button_width = 200
        button_height = 50
        button_margin = 20
        x = WIDTH // 2
        y = 200  # Adjusted the y position to position buttons higher

        login_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, login_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, login_button_rect)
        draw_text("Login", button_font, BLACK, screen, x, y + button_height // 2)

        y += button_height + button_margin
        signup_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, signup_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, signup_button_rect)
        draw_text("Signup", button_font, BLACK, screen, x, y + button_height // 2)

        y += button_height + button_margin
        scoreboard_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, scoreboard_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, scoreboard_button_rect)
        draw_text("Scoreboard", button_font, BLACK, screen, x, y + button_height // 2)

        y += button_height + button_margin
        tutorial_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, tutorial_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, tutorial_button_rect)
        draw_text("Tutorial", button_font, BLACK, screen, x, y + button_height // 2)

        y += button_height + button_margin
        exit_button_rect = pygame.Rect(x - button_width // 2, y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, exit_button_rect, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, exit_button_rect)
        draw_text("Exit", button_font, BLACK, screen, x, y + button_height // 2)

        # Draw the credits text
        credits = [
            "Developed by:",
            "Rafey Islam",
            "Suijith Ravichandran",
            "Shehrina Hossain",
            "Sarim Khan",
            "Rawad Alharastani",
            "Team 6",
            "Winter 2024",
            "CS 2212 Western University"
        ]

        # Start drawing from the bottom left going up
        y_pos = HEIGHT - 10
        credit_spacing = 5
        credit_height = credit_font.size("Test")[1]
        for line in reversed(credits):
            credit_text = credit_font.render(line, True, BLACK)
            credit_text_height = credit_text.get_height()
            y_pos -= (credit_text_height + credit_spacing)

            # Draw white box around the credit text
            credit_box_rect = pygame.Rect(10, y_pos, credit_text.get_width(), credit_text_height)
            pygame.draw.rect(screen, WHITE, credit_box_rect)

            # Blit the credit text
            screen.blit(credit_text, (10, y_pos))


        pygame.display.flip()


if __name__ == "__main__":
    main_menu(screen, title_font, button_font, WHITE, BLACK, LIGHT_GRAY, WIDTH, HEIGHT)

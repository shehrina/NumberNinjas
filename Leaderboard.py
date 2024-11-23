import pygame
import pandas as pd
import sys
from savedata import savedata
def Leaderboard():
    # Initialize Pygame
    """
    🌟 Display the game's leaderboard with top player scores.

    This function creates a leaderboard screen using Pygame and displays the top scores fetched from
    the saved data. It allows players to see who's leading in the game and motivates them to improve
    their own scores.

    Attributes:
        SCREEN_WIDTH (int): Width of the leaderboard screen in pixels.
        SCREEN_HEIGHT (int): Height of the leaderboard screen in pixels.
        WHITE, BLACK, BUTTON_COLOR (tuple): RGB color codes used for the screen's background, text, and buttons.

    Returns:
        'back' (str): A string flag to indicate when the user wants to navigate back to the previous screen.

    """
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_COLOR = (150, 150, 150)  # Color of the button rectangle

    # Font
    FONT_SIZE = 24
    font = pygame.font.Font(None, FONT_SIZE)

    # Load your player data into a pandas dataframe
    saves = savedata()
    top5 = saves.getHighScores()

    # Pygame setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Leaderboard")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 60, 100, 40)
                if button_rect.collidepoint(mouse_pos):
                    print("Back button clicked!") 
                    return 'back' # Placeholder for button functionality
                    # Add your functionality here

        # Display leaderboard
        screen.fill(WHITE)
        header_text = font.render("Leaderboard", True, BLACK)
        screen.blit(header_text, (SCREEN_WIDTH // 2 - header_text.get_width() // 2, 20))
        y_position = 70

        for index, row in top5.iterrows():
            player_text = font.render(f"{row['Username']}: {row['Score']}", True, BLACK)
            screen.blit(player_text, (SCREEN_WIDTH // 2 - player_text.get_width() // 2, y_position))
            y_position += FONT_SIZE + 5

        # Render Back button
        back_text = font.render("Back", True, BLACK)
        back_rect = back_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        pygame.draw.rect(screen, BUTTON_COLOR, back_rect.inflate(10, 5))  # Draw a rectangle around the text
        screen.blit(back_text, back_rect)

        pygame.display.flip()
        pygame.time.delay(100)  # Adjust the delay as needed to control frame rate

def OpenLeaderboard(User=None):
    """
    Open the leaderboard screen to display high scores.
    
    Call this function to transition from the main game to the leaderboard.
    """
    Leaderboard()

if __name__ == "__main__":
    """
    When this module is executed as the main program, it will display the leaderboard immediately,
    allowing players to see the highest scores without navigating through the game menus.
    """
    Leaderboard()



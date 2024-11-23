import sys
import pygame
from OpeneingScreen import main_menu
from SignInPage import OpenSignInPage
from SignUpPage import OpenSignUpPage
from Leaderboard import OpenLeaderboard, Leaderboard
from Tutorial import main

class Game:
    """
    🎮 The `Game` class is the heart of Number Ninjas, orchestrating the game's flow. 🕹️

    Attributes:
        screen (pygame.Surface): The main display surface for the game.
        current_screen (str): Tracks the current screen or stage of the game.
        title_font (pygame.font.Font): Font for rendering the game's title.
        button_font (pygame.font.Font): Font for buttons and interactive elements.
        WHITE, BLACK, LIGHT_GRAY (tuple): Color definitions for various UI elements.
        WIDTH, HEIGHT (int): Dimensions for the game window.
        logged_in_user: The currently logged-in user's data.

    Methods:
        switch_to_signin(): Attempt to sign in a user and handle navigation.
        run(): The main loop that keeps the game running and responsive.
    """
    def __init__(self):
        """
        Initializes the game, setting up the screen, fonts, colors, and the starting screen. 🛠️
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.current_screen = 'opening'
        self.title_font = pygame.font.Font(None, 72)
        self.button_font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (150, 150, 150)
        self.WIDTH = 800
        self.HEIGHT = 600
        self.logged_in_user = None

    def switch_to_signin(self):
        """
        Handles switching to the sign-in screen and manages user login flow. 🔑
        Returns a string indicating navigation flow based on sign-in actions.
        """
        result = OpenSignInPage()
        if result == 'back':
            return 'back'
        elif result:
            self.logged_in_user = result
            return 'opening'

    def run(self):
        """
        The main event loop of the game. This method keeps the game alive and kicking! 🔄
        It listens for events and changes the current screen based on game logic.
        """
        while True:
            if self.current_screen == 'opening':
                next_screen = main_menu(self.screen, self.title_font, self.button_font, self.WHITE, self.BLACK, self.LIGHT_GRAY, self.WIDTH, self.HEIGHT)
                if next_screen:
                    self.current_screen = next_screen

            elif self.current_screen == 'signin':
                result = self.switch_to_signin()
                if result == 'back':
                    self.current_screen = 'opening'

            elif self.current_screen == 'signup':
                result = OpenSignUpPage()
                if result == 'back':
                    self.current_screen = 'opening'
                elif result == 'signin':
                    self.current_screen = 'signin'
                    
            elif self.current_screen == 'scoreboard':
                result = Leaderboard()
                if result == 'back':
                    self.current_screen = 'opening'
            elif self.current_screen == 'tutorial':
                result = main(self.screen)
                if result == 'back':
                    self.current_screen = 'opening'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()

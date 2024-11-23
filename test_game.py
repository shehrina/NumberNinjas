#TO RUN THIS TEST, ONCE THE GAME IS INITALIZED AND YOU SEE A BLACK WINDON YOU MAY JUST CLICK ANYWHERE IN THE WINDOW 
#AND THE TEST WILL TERMINATE 

import unittest
from unittest.mock import patch, MagicMock

class TestGameRunMethod(unittest.TestCase):
    def setUp(self):
        # Patch the entire 'pygame' module
        self.patcher_pygame = patch('Game.pygame')
        self.mock_pygame = self.patcher_pygame.start()
        self.mock_pygame.QUIT = 0
        self.mock_pygame.event.get.return_value = []

        from Game import Game
        self.game = Game()
        self.game.screen = MagicMock()  

    def tearDown(self):
        self.patcher_pygame.stop()

    def simulate_quit_event(self):
        mock_event = MagicMock()
        mock_event.type = self.mock_pygame.QUIT
        self.mock_pygame.event.get.return_value = [mock_event]

    def test_main_menu_to_signin(self):
        with patch('Game.main_menu', return_value='signin'), \
             patch.object(self.game, 'switch_to_signin', return_value=None):
            self.game.current_screen = 'opening'
            self.simulate_quit_event()
            with self.assertRaises(SystemExit):
                self.game.run()
            self.assertEqual(self.game.current_screen, 'signin')

    def test_main_menu_to_signup(self):
        with patch('Game.main_menu', return_value='signup'), \
             patch('Game.OpenSignUpPage', return_value=None):
            self.game.current_screen = 'opening'
            self.simulate_quit_event()
            with self.assertRaises(SystemExit):
                self.game.run()
            self.assertEqual(self.game.current_screen, 'signup')

    def test_main_menu_to_tutorial(self):
        with patch('Game.main_menu', return_value='tutorial'), \
             patch('Game.main', return_value='back'):
            self.game.current_screen = 'opening'
            self.simulate_quit_event()
            with self.assertRaises(SystemExit):
                self.game.run()
            self.assertEqual(self.game.current_screen, 'tutorial')

    def test_main_menu_to_scoreboard(self):
        with patch('Game.main_menu', return_value='scoreboard'), \
             patch('Game.Leaderboard', return_value='back'):
            self.game.current_screen = 'opening'
            self.simulate_quit_event()
            with self.assertRaises(SystemExit):
                self.game.run()
            self.assertEqual(self.game.current_screen, 'scoreboard')

    def test_run_exit(self):
        self.simulate_quit_event()
        with patch('pygame.draw.rect'): 
            with self.assertRaises(SystemExit):
                self.game.run()
        self.mock_pygame.quit.assert_called_once()



if __name__ == '__main__':
    unittest.main()

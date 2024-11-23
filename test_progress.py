import unittest
from unittest.mock import patch, MagicMock
import pygame

sys = MagicMock()
Student = MagicMock()

pygame.init = MagicMock()
pygame.display.set_mode = MagicMock()
pygame.display.set_caption = MagicMock()
pygame.font.Font = MagicMock()
pygame.draw.rect = MagicMock()
pygame.draw.line = MagicMock()

from progress import progress_main, draw_progress_screen, draw_levels

class TestProgressScreen(unittest.TestCase):
    def setUp(self):
        self.student = MagicMock()
        self.student.getScore.return_value = 5

    @patch('pygame.event.get')
    def test_quit_event(self, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]
        with self.assertRaises(SystemExit):
            progress_main(self.student)

    @patch('pygame.event.get')
    @patch('pygame.mouse.get_pos')
    def test_back_button_click(self, mock_get_pos, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.MOUSEBUTTONDOWN)]
        mock_get_pos.return_value = (800 - 10, 600 - 10)  # Position of the back button
        with self.assertRaises(SystemExit):
            progress_main(self.student)

    @patch('pygame.font.Font.render')
    def test_current_level_display(self, mock_render):
        draw_progress_screen(self.student)
        current_level_text = f"Current Level: {self.student.getScore() + 1}"
        mock_render.assert_any_call(current_level_text, True, (0, 0, 0))

    @patch('pygame.font.Font.render')
    def test_questions_solved_display(self, mock_render):
        draw_progress_screen(self.student)
        questions_solved_text = f"Questions Solved: {self.student.getScore() * 5}"
        mock_render.assert_any_call(questions_solved_text, True, (0, 0, 0))

    @patch('pygame.draw.rect')
    def test_level_colors(self, mock_draw_rect):
        draw_levels(self.student.getScore())
        self.assertEqual(mock_draw_rect.call_args_list[0][0][1], (0, 255, 0))  
        self.assertEqual(mock_draw_rect.call_args_list[2][0][1], (0, 255, 0))  
        self.assertEqual(mock_draw_rect.call_args_list[4][0][1], (0, 255, 0))  
        self.assertEqual(mock_draw_rect.call_args_list[6][0][1], (255, 255, 255))  

if __name__ == '__main__':
    unittest.main()

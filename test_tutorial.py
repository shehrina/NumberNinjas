import unittest
from Tutorial import MathQuestion, Room, Enemy

class TestTutorial(unittest.TestCase):
    def test_math_question_generation(self):
        question = MathQuestion(1)
        question.generate_question('+', 0, 10)
        self.assertIn('+', question.equation)

    def test_question_check_answer_correct(self):
        question = MathQuestion(1)
        question.equation = "What is 2 + 2?"
        question.answer = 4
        self.assertIn("Good job!", question.check_answer(4))

    def test_question_check_answer_incorrect(self):
        question = MathQuestion(1)
        question.equation = "What is 2 + 2?"
        question.answer = 4
        incorrect_feedback = ["Needs some work!", "Better luck next time!", "You'll see me again soon!", "Oh no!"]
        self.assertIn(question.check_answer(5), incorrect_feedback)

    def test_enemy_initialization(self):
        question = MathQuestion(1)
        enemy = Enemy(question)
        self.assertEqual(enemy.equation, question)

    def test_room_initialization(self):
        room = Room(1)
        self.assertEqual(room.diff, 1)

    def test_room_add_question(self):
        room = Room(1)
        question = MathQuestion(1)
        room.add_question(question)
        self.assertIn(question, room.questions)

    def test_room_timer(self):
        room = Room(1)
        room.start_timer()
        room.stop_timer()
        self.assertEqual(room.get_time_spent(), 0)

if __name__ == '__main__':
    unittest.main()




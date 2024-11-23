import unittest
from savedata import savedata
from MathQuestion import MathQuestion
from Student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student()

    def test_answer_correct(self):
        question = MathQuestion(1)  # Create MathQuestion instance with difficulty
        question.generate_question('+', 1, 10)  # Generate a question
        correct_answer = question.answer  # Get the correct answer
        self.assertTrue(self.student.answer(question, correct_answer))

    def test_answer_incorrect(self):
        question = MathQuestion('easy')  # Create MathQuestion instance with difficulty
        question.generate_question('+', 1, 10)  # Generate a question
        correct_answer = question.answer  # Get the correct answer
        self.assertFalse(self.student.answer(question, correct_answer + 1))  # Answer incorrectly

    def test_signup(self):
        data = savedata()
        data.deleteUserData("testforunittest")
        self.assertTrue(self.student.signup("testforunittest", "password", "email@example.com", data))

    def test_signin(self):
        data = savedata()
        data.addNewUser("username", "password", "email@example.com", 'Student')
        self.student.signin("username", "password", data)
        self.assertEqual(self.student.getUserName(), "username")

    def test_next_level(self):
        self.student.nextLevel()
        self.assertEqual(self.student.getScore(), 1)

if __name__ == '__main__':
    unittest.main()
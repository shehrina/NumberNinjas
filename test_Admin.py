import unittest
from unittest.mock import MagicMock
import sys
import random
from savedata import savedata
from Student import Student
from Teacher import Teacher
from Admin import Admin
from MathQuestion import MathQuestion

class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin()
        self.save_data = savedata()

    def test_answer_correct(self):
        question = MathQuestion(1)
        question.equation = "What is 2 + 2?"
        question.answer = 4
        positive_feedback = ["Good job!", "Nice one!", "Well done!","Awesome!"]
        self.assertIn(question.check_answer(4), positive_feedback)

    def test_answer_incorrect(self):
        question = MathQuestion(1)
        question.equation = "What is 2 + 2?"
        question.answer = 4
        negative_feedback = ["Needs some work!", "Better luck next time!", "You'll see me again soon!", "Oh no!"]
        self.assertIn(question.check_answer(5), negative_feedback)
    
    def test_signup(self):
        data = savedata()
        data.deleteUserData("admin1")
        self.assertTrue(self.admin.signup("admin1", "password", "admin1@example.com", data))

    def test_sign_in(self):
        data = savedata()
        data.addNewUser("admin1", "password", "admin1@example.com", 'Admin')
        self.admin.signin("admin1", "password", data)
        self.assertEqual(self.admin.username, "admin1")
        self.assertEqual(self.admin.email, "admin1@example.com")

if __name__ == '__main__':
    unittest.main()

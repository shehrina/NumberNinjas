import pytest
from MathQuestion import MathQuestion

# Test the MathQuestion class
class TestMathQuestion:
    @pytest.fixture
    def math_question(self):
        return MathQuestion(1)  # Create an instance of MathQuestion with difficulty 1

    def test_initialization(self, math_question):
        assert math_question.equation == ""  # Equation should be empty initially
        assert math_question.answer == 0  # Answer should be 0 initially
        assert math_question.difficulty == 1  # Difficulty should be 1 initially

    def test_set_question(self, math_question):
        math_question.set_question("What is 2 + 2?")
        assert math_question.equation == "What is 2 + 2?"

    def test_get_question(self, math_question):
        math_question.set_question("What is 2 + 2?")
        assert math_question.get_question() == "What is 2 + 2?"

    def test_set_difficulty(self, math_question):
        math_question.set_difficulty(2)
        assert math_question.difficulty == 2

    def test_get_difficulty(self, math_question):
        assert math_question.get_difficulty() == 1

    def test_generate_question(self, math_question):
        math_question.generate_question('+', 1, 10)
        assert math_question.equation.startswith("What is ")
        assert math_question.equation.endswith("?")

    def test_check_answer_correct(self, math_question):
        math_question.answer = 4
        assert math_question.check_answer(4) == "Good job!" or math_question.check_answer(4) == "Nice one!" or math_question.check_answer(4) == "Well done!" or math_question.check_answer(4) == "Awesome!"

    def test_check_answer_incorrect(self, math_question):
        math_question.answer = 4
        assert math_question.check_answer(3) == "Needs some work!" or math_question.check_answer(3) == "Better luck next time!" or math_question.check_answer(3) == "You'll see me again soon!" or math_question.check_answer(3) == "Oh no!"


import pytest
from Enemy import Enemy

@pytest.fixture
def math_question():
    class MathQuestion:
        def __init__(self, equation):
            self.equation = equation

    return MathQuestion(equation="What is 2 + 3?")

@pytest.fixture
def enemy(math_question):
    return Enemy(equation=math_question)

def test_print_lose_message(capsys, enemy):
    enemy.print_lose_message()
    captured = capsys.readouterr()
    assert captured.out.strip() in ["Needs some work!", "Better luck next time!", "You'll see me again soon!", "Oh no!"]

def test_print_win_message(capsys, enemy):
    enemy.print_win_message()
    captured = capsys.readouterr()
    assert captured.out.strip() in ["Good job!", "Nice one!", "Well done!", "Awesome!"]

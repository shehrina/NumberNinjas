import pytest
from MainGamePage import generate_questions

def test_generate_questions():
    # Test for a simple case, ensuring the correct number of questions are generated
    questions = generate_questions(1, 5)
    assert len(questions) == 5

    for difficulty in range(1, 6):
        questions = generate_questions(difficulty, 1)
        assert len(questions) == 1
        

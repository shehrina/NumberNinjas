import pytest 
import pygame
from Room import Room 

@pytest.fixture
def room():
    pygame.init()
    return Room(3)

def test_room_initialization(room):
    assert room.diff == 3
    assert len(room.questions) == 0
    assert room.time == 0

def test_add_question(room):
    question = "What is 5 + 2?"
    room.add_question(question)
    assert len(room.questions) == 1
    assert room.questions[0] == question

def test_start_timer(room):
    room.start_timer()
    assert room.time != 0

def test_stop_timer(room):
    room.start_timer()
    room.stop_timer()
    assert room.time == 0
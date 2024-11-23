import pytest
import pygame
from SignInPage import TextBox, RadioButton, MessageBox

def test_textbox_initialization():
    textbox = TextBox((250, 120, 300, 30), "test")
    assert textbox.text == "test"
    assert textbox.rect.size == (300, 30)

def test_textbox_deactivation():
    textbox = TextBox((250, 120, 300, 30))
    textbox.active = True
    textbox.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    assert not textbox.active

def test_radiobutton_initialization():
    radiobutton = RadioButton((250, 120, 20, 20), "Option")
    assert radiobutton.text == "Option"
    assert radiobutton.rect.size == (20, 20)

def test_radiobutton_selection():
    radiobutton = RadioButton((250, 120, 20, 20))
    radiobutton.handle_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(255, 125)))
    assert radiobutton.selected

def simulate_text_input(textbox, input_text):
    for char in input_text:
        textbox.handle_event(pygame.event.Event(pygame.KEYDOWN, unicode=char, key=ord(char)))
    textbox.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))

def simulate_button_click(button):
    button['action']()

def test_sign_in_invalid_credentials():
    username_box = TextBox((250, 120, 300, 30))
    password_box = TextBox((250, 170, 300, 30))
    message_box = MessageBox((50, 330, 700, 50))
    sign_in_button = {'action': lambda: setattr(message_box, 'text', "Invalid username or password.")}

    simulate_text_input(username_box, "invalid_username")
    simulate_text_input(password_box, "invalid_password")
    simulate_button_click(sign_in_button)
    assert message_box.text == "Invalid username or password."





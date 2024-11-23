import pygame
import random 

class Enemy:
    """
    A class to represent an enemy, encapsulating its difficulty level and an associated math equation.

    Attributes:
        diff (int): The difficulty level of the enemy. Initially set to 1.
        equation (MathQuestion): The math question associated with the enemy.
    """

    def __init__(self, equation, is_boss=False):
        """
        Constructs all the necessary attributes for the enemy object.

        Parameters:
            equation (MathQuestion): The math question associated with this enemy.
        """
        self.diff = 1
        self.equation = equation
        self.is_boss = is_boss

    def print_lose_message(self):
        """
        Prints a random lose message from the list, indicating the player's defeat.
        """
        negative_feedback = random.choice(
            ["Needs some work!", "Better luck next time!", "You'll see me again soon!", "Oh no!"])
        print(negative_feedback)

    def print_win_message(self):
        """
        Prints a random win message from the list, celebrating the player's victory.
        """
        positive_feedback = random.choice(["Good job!", "Nice one!", "Well done!", "Awesome!"])
        print(positive_feedback)

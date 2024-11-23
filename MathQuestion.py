import pygame
import random

class MathQuestion:
    """
    🧮 The MathQuestion class generates and manages mathematical challenges for Number Ninjas. 🥋

    Attributes:
        equation (str): The mathematical equation in string format.  
        answer (int): The correct answer to the equation.  
        difficulty (int): The difficulty level of the question.

    Methods:
        set_question: Updates the equation with a new question.  
        get_question: Returns the current math equation.  
        set_difficulty: Adjusts the difficulty level of the question.  
        get_difficulty: Retrieves the current difficulty level.  
        generate_question: Dynamically creates a math question based on the operation and number range.  
        check_answer: Validates the player's answer, providing encouraging feedback.
    """

    def __init__(self, difficulty):
        """
        Initializes a new MathQuestion instance with a specified difficulty level.

        Parameters:  
            difficulty (int): The initial difficulty level for the math question.
        """
        self.equation = ""
        self.answer = 0
        self.difficulty = difficulty

    def set_question(self, new_question):
        """
        Updates the equation attribute, setter method.

        Parameters:  
            new_question (str): The new math equation to be set.
        """
        self.equation = new_question

    def get_question(self):
        """
        Returns the current math equation as a string, getter method.

        Returns:  
            str: The current math equation.
        """
        return self.equation

    def set_difficulty(self, new_difficulty):
        """
        Adjusts the difficulty level, setter method.

        Parameters:  
            new_difficulty (int): The new difficulty level to be set.
        """
        self.difficulty = new_difficulty

    def get_difficulty(self):
        """
        Retrieves the current difficulty level, getter method.

        Returns:  
            int: The difficulty level of the math question.
        """
        return self.difficulty

    def generate_question(self, operation, min, max):
        """
        Dynamically generates a new math question based on the given parameters.

        Parameters:  
            operation (str): The mathematical operation to be used ('+', '-', '*', '/').  
            min (int): The minimum value for the generated numbers.  
            max (int): The maximum value for the generated numbers.
        """

        num1 = random.randint(min, max)
        num2 = random.randint(min, max)

        if operation == '+':
            self.equation = f"What is {num1} + {num2}?"
            self.answer = num1 + num2
        elif operation == '-':
            if num1 < num2:  # makes sure the answer is not negative
                num1, num2 = num2, num1
            self.equation = f"What is {num1} - {num2}?"
            self.answer = num1 - num2
        elif operation == '*':
            self.equation = f"What is {num1} * {num2}?"
            self.answer = num1 * num2
        elif operation == '/':
            if num2 == 0:  # avoid division by zero
                num2 = 1
            if num1 == 0:
                num1 == 1
            result = (num1 * num2) / num2 # makes sure the answer the user inputs will always be a natural number
            num3 = num1 * num2
            self.equation = f"What is {num3} / {num2}?"
            self.answer = int(result)

    def check_answer(self, user_answer):
        """
        Validates the user's answer to the math question, providing feedback.

        Parameters:  
            user_answer (int): The answer provided by the user.

        Returns:  
            str: Feedback message based on the correctness of the user's answer.
        """
        if user_answer == self.answer:
            positive_feedback = random.choice(["Good job!", "Nice one!", "Well done!","Awesome!"])
            print(positive_feedback)
            return positive_feedback
        else:
            negative_feedback = random.choice(["Needs some work!", "Better luck next time!", "You'll see me again soon!","Oh no!"])
            print(negative_feedback)
            return negative_feedback


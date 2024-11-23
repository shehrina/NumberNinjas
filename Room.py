import pygame
class Room:
    """
    Represents a room within the game, which contains a series of math questions
    for the player to solve. Each room has a difficulty level and tracks the time
    spent on the current question.
    
    Attributes:
        diff (int): The difficulty level of the room.
        questions (list): A list of math questions assigned to the room.
        time (int): The starting time when the timer is activated for the current question.
        current_question_index (int): The index of the current question being displayed.
    """
    def __init__(self, diff):
        """
        Initializes a new Room instance with a specified difficulty level.
        
        Parameters:
            diff (int): The difficulty level of the room.
        """
        self.diff = diff
        self.questions = []
        self.time = 0
        self.current_question_index = 0

    def add_question(self, question):
        """
        Adds a new question to the room.
        
        Parameters:
            question: The math question to be added to the room.
        """
        self.questions.append(question)

    def start_timer(self):
        """
        Starts the timer by recording the current time.
        """
        self.time = pygame.time.get_ticks()

    def stop_timer(self):
        """
        Stops the timer by setting the time attribute to 0.
        """
        self.time = 0

    def get_time_spent(self):
        """
        Calculates and returns the time spent on the current question in milliseconds.
        
        Returns:
            int: The time spent on the current question in milliseconds. Returns 0 if the timer was not started.
        """
        if self.time:
            return pygame.time.get_ticks() - self.time
        return 0

from PlayerInterface import PlayerInterface
import MathQuestion
import savedata
class Admin(PlayerInterface):
    """
    Represents an administrator for the Number Ninjas game. Admins have the power to create and manage content within the game.

    Inherits from:
    - PlayerInterface: This class inherits from the PlayerInterface to utilize common player functionalities.

    Methods:
    - answer: Allows the admin to provide answers to math questions.
    - signup: Registers a new admin account in the game's database.
    - signin: Authenticates an admin returning to the game.
    """
    def __init__(self):
        """
        Initializes a new admin instance with empty credentials.
        """
        self.username = ""
        self.password = ""
        self.email = ""

    def answer(self, q: MathQuestion, a: int):
        """
        Evaluates an answer to a given math question.

        Parameters:
        - q (MathQuestion): The math question to be answered.
        - a (int): The answer provided by the admin.

        Returns:
        - bool: True if the answer is correct, False otherwise.
        """
        return q.checkAnswer(a)

    def signup(self, username, password, email, saves: savedata):
        """
        Registers a new admin with the provided credentials.

        Parameters:
        - username (str): The admin's chosen username.
        - password (str): The admin's chosen password.
        - email (str): The admin's email address.
        - saves (savedata): A reference to the savedata module for accessing the database.

        Returns:
        - bool: True if registration is successful, False otherwise.
        """
        self.username = username
        self.password = password
        self.email = email
        return saves.addNewUser(username, password, email, 'Admin')

    def signin(self, username, password, saves: savedata):
        """
        Authenticates an admin attempting to sign in.

        Parameters:
        - username (str): The admin's username.
        - password (str): The admin's password.
        - saves (savedata): A reference to the savedata module for accessing the database.

        Returns:
        - bool: True if authentication is successful, False otherwise.
        """
        userData = saves.getUserData(username, password)
        if userData == None:
            return False
        self.username = userData['Username']
        self.password = userData['Password']
        self.email = userData['Email']



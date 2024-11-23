from PlayerInterface import PlayerInterface
import MathQuestion
import savedata
class Student(PlayerInterface):
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.highscore = 0

    def answer(self, q: MathQuestion, a: int):
        if q.check_answer(a) == "Good job!" or q.check_answer(a) == "Nice one!" or q.check_answer(a) == "Well done!" or q.check_answer(a) == "Awesome!":
            return True
        else:
            return False

    def signup(self, username: str, password: str, email: str, data: savedata):
        self.username = username
        self.password = password
        self.email = email
        self.highscore = 0
        return data.addNewUser(username, password, email, 'Student')

    def signin(self, username: str, password: str, saves: savedata):
        userData = saves.getUserData(username, password)
        if userData == None:
            return False
        self.username = userData['Username']
        self.password = userData['Password']
        self.email = userData['Email']
        self.highscore = userData['Score']

    def nextLevel(self):
        self.highscore+=1

    def getScore(self):
        return self.highscore

    def getUserName(self):
        return self.username
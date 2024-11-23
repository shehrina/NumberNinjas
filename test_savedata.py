from savedata import *
from Student import Student
import unittest
import pandas as pd

class test_savedata(unittest.TestCase):

    def test_constructor(self):
        try:
            saves = savedata()
            self.assertTrue(True)
        except FileNotFoundError:
            self.fail("Error: File not found.")
        except Exception as e:
            self.fail("An error occurred:", e)

    def test_addNewUser(self):
        saves = savedata()
        username = "George"
        password = "woqeqpiw"
        email = "george12@gmail.com"
        usertype = "Student"

        added = saves.addNewUser(username, password, email, usertype)
        saves.deleteUserData("George")
        self.assertTrue(added, True)

    def test_saveGame(self):
        saves = savedata()
        username = "Paul"
        password = "eqweq"
        email = "paul37@gmail.com"

        paul = Student()
        paul.signup(username, password, email, saves)

        paul.nextLevel()

        saves.saveGame(paul)
        paulData = saves.getUserData(username, password)
        saves.deleteUserData(username)
        self.assertEqual(paulData['Score'], 1)

    def test_getUserData(self):
        saves = savedata()
        username = "Paul"
        password = "eqweq"
        email = "paul37@gmail.com"

        paul = Student()
        paul.signup(username, password, email, saves)

        paulData = saves.getUserData(username, password)
        isNone = paulData == None
        saves.deleteUserData(username)
        self.assertFalse(isNone)

    def test_getDataframe(self):
        saves = savedata()
        df = saves.getDataframe()
        self.assertIsInstance(df, pd.DataFrame)

    def test_getHighScores(self):
        saves = savedata()
        highscores = saves.getHighScores()
        scores = highscores['Score'].tolist()
        next = scores[0]
        scores = scores[1:]
        for score in scores:
            if next < score:
                self.fail("Not a valid high score list.")
            next = score

        self.assertTrue(True)

    def test_deleteUserData(self):
        saves = savedata()
        username = "Paul"
        password = "eqweq"
        email = "paul37@gmail.com"

        paul = Student()
        paul.signup(username, password, email, saves)
        saves.deleteUserData(username)
        paulData = saves.getUserData(username, password)

        isNone = paulData == None
        self.assertTrue(isNone)




if __name__ == '__main__':
    unittest.main()
from PlayerInterface import PlayerInterface
import savedata
class Teacher(PlayerInterface):
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""

    def signup(self, username: str, password: str, email: str, data: savedata):
        self.username = username
        self.password = password
        self.email = email
        return data.addNewUser(username, password, email, 'Teacher')

    def signin(self, username: str, password: str, data: savedata):
        userData = data.getUserData(username, password)
        if userData == None:
            return False
        self.username = userData['Username']
        self.password = userData['Password']
        self.email = userData['Email']

    def deleteStudent(self, username: str, data: savedata):
        data.deleteUserData(username)
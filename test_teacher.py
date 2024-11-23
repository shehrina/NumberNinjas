import unittest
from savedata import savedata
from Teacher import Teacher

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher()

    def test_signup(self):
        data = savedata()
        data.deleteUserData("teacher1")
        self.assertTrue(self.teacher.signup("teacher1", "password", "teacher1@example.com", data))

    def test_signin(self):
        data = savedata()
        data.addNewUser("teacher1", "password", "teacher1@example.com", 'Teacher')
        self.teacher.signin("teacher1", "password", data)
        self.assertEqual(self.teacher.username, "teacher1")
        self.assertEqual(self.teacher.email, "teacher1@example.com")

    def test_deleteStudent(self):
        data = savedata()
        data.addNewUser("student1", "password", "student1@example.com", 'Student')
        self.teacher.deleteStudent("student1", data)
        self.assertIsNone(data.getUserData("student1", "password"))

if __name__ == '__main__':
    unittest.main()
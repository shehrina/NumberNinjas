from SignUpPage import *
import unittest

username_box = TextBox((250, 120, 300, 30))
password_box = TextBox((250, 170, 300, 30))
email_box = TextBox((250, 220, 300, 30))
text_boxes = [username_box, password_box, email_box]

# Radio buttons initialization
student_button = RadioButton((250, 280, 150, 30), "Student")
teacher_button = RadioButton((400, 280, 150, 30), "Teacher")
moderator_button = RadioButton((550, 280, 150, 30), "Moderator")
radio_buttons = [student_button, teacher_button, moderator_button]

def sign_up():
    # Add functionality for sign-up button
    username = username_box.get_text()
    password = password_box.get_text()
    email = email_box.get_text()

    usertype = ""
    for button in radio_buttons:
        if button.is_selected():
            usertype = button.getText()

    if usertype == "" or username == "" or password == "" or email == "":
        message_box.text = "Missing fields required."
    else:
        saves = savedata()
        if usertype == 'Student':
            user = Student()
        elif usertype == 'Teacher':
            user = Teacher()
        else:
            user = Admin()

        if user.signup(username, password, email, saves) == False:
            message_box.text = "Username is taken."

        else:
            message_box.text = "Sign Up Successful."

class test_SignUpPage(unittest.TestCase):

    def test_successful_sign_up(self):
        username_box.text = 'Bob'
        password_box.text = 'Ross'
        email_box.text = 'bobross@gmail.com'
        student_button.selected = True

        sign_up()
        saves = savedata()
        saves.deleteUserData("Bob")
        self.assertEqual(message_box.text, "Sign Up Successful.")


    def test_username_taken(self):
        username_box.text = 'suji'
        password_box.text = 'Ross'
        email_box.text = 'bobross@gmail.com'
        student_button.selected = True

        sign_up()
        self.assertEqual(message_box.text, "Username is taken.")

    def test_missing_field(self):
        username_box.text = 'suji'
        sign_up()
        self.assertEqual(message_box.text, "Missing fields required.")

if __name__ == '__main__':
    unittest.main()


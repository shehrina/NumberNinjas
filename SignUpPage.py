import pygame
import time
import sys
import SignInPage
from savedata import savedata
from Student import Student
from Teacher import Teacher
from Admin import Admin
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

FONT = pygame.font.Font(None, 32)

# Textbox class
class TextBox:
    """
    Represents a textbox for user input in a Pygame application.

    Attributes:
        rect (pygame.Rect): The rectangle area of the textbox.
        text (str): The current text displayed in the textbox.
        txt_surface (pygame.Surface): The surface that the text is rendered on.
        active (bool): Indicates whether the textbox is currently active.
    """
    def __init__(self, rect, text=''):
        """
        Initializes a new instance of TextBox.
        
        Parameters:
            rect (tuple): The rectangle defining the textbox's position and size.
            text (str, optional): Initial text to display in the textbox.
        """
        self.rect = pygame.Rect(rect)
        self.color = BLACK
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        Handles events for the textbox, including mouse clicks and keyboard inputs.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the textbox
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the color of the textbox
            self.color = BLACK if self.active else GRAY
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, surface):
        """
        Draws the textbox on a given surface.

        Parameters:
            surface (pygame.Surface): The surface on which to draw the textbox.
        """
        pygame.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        """
        Returns the current text of the textbox.
        """
        return self.text
# Function to draw text on the screen
def draw_text(surface, text, color, rect, font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = rect.center
    surface.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(surface, rect, color, text, font):
    pygame.draw.rect(surface, color, rect)
    draw_text(surface, text, BLACK, rect, font)

# Function to handle input events
def handle_input(events, text_boxes, buttons):
    for box in text_boxes:
        for event in events:
            box.handle_event(event)

    for button in buttons:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button['rect'].collidepoint(event.pos):
                    button['action']()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


# Radio button class
class RadioButton:
    """
    Represents a radio button for selecting options in a Pygame application.

    Attributes:
        rect (pygame.Rect): The rectangle area of the radio button.
        text (str): The label text of the radio button.
        selected (bool): Indicates whether the radio button is selected.
    """
    def __init__(self, rect, text=''):
        """
        Initializes a new instance of RadioButton.

        Parameters:
            rect (tuple): The rectangle defining the radio button's position and size.
            text (str, optional): The label text of the radio button.
        """

        self.rect = pygame.Rect(rect)
        self.color = BLACK
        self.text = text
        self.font = FONT
        self.selected = False

    def handle_event(self, event):
        """
        Handles events for the radio button, including mouse clicks.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = True
            else:
                self.selected = False

    def draw(self, surface):
        """
        Draws the radio button on a given surface.

        Parameters:
            surface (pygame.Surface): The surface on which to draw the radio button.
        """
        pygame.draw.rect(surface, self.color, self.rect, 2)
        if self.selected:
            pygame.draw.circle(surface, self.color, (self.rect.x + 10, self.rect.y + 10), 6)

        # Calculate text position to center it within the button
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect.topleft)

    def is_selected(self):
        """
        Checks if the radio button is selected.

        Returns:
            bool: True if the radio button is selected, False otherwise.
        """
        return self.selected

    def getText(self):
        """
        Returns the label text of the radio button.
        """
        return self.text

class MessageBox:
    """
    Represents a message box for displaying text messages in a Pygame application.

    Attributes:
        rect (pygame.Rect): The rectangle area of the message box.
        text (str): The message text to display.
        text_color (tuple): The color of the message text.
    """
    def __init__(self, rect):
        """
        Initializes a new instance of MessageBox.

        Parameters:
            rect (tuple): The rectangle defining the message box's position and size.
        """
        self.rect = pygame.Rect(rect)
        self.color = WHITE
        self.text = ""
        self.text_color = (255,0,0)

    def draw(self, surface):
        """
        Draws the message box and its text on a given surface.

        Parameters:
            surface (pygame.Surface): The surface on which to draw the message box.
        """
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text:
            draw_text(surface, self.text,self.text_color, self.rect, FONT)

# Function to display sign up screen
FONT_TITLE = pygame.font.Font(None, 48)
def sign_up_screen(text_boxes, buttons, radio_buttons,screen):
    screen.fill(WHITE)
    # Draw the title "Number Ninjas"
    draw_text(screen, "Number Ninjas", BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, 100), FONT_TITLE)
    # Draw input fields for username, password, email
    draw_text(screen, "Sign Up", BLACK, pygame.Rect(0, 75, SCREEN_WIDTH, 50), FONT)
    draw_text(screen, "Username:", BLACK, pygame.Rect(50, 120, 200, 30), FONT)
    text_boxes[0].draw(screen)
    draw_text(screen, "Password:", BLACK, pygame.Rect(50, 170, 200, 30), FONT)
    text_boxes[1].draw(screen)
    draw_text(screen, "Email:", BLACK, pygame.Rect(50, 220, 200, 30), FONT)
    text_boxes[2].draw(screen)
    # Draw radio buttons for options
    draw_text(screen, "Choose Role:", BLACK, pygame.Rect(50, 270, 200, 30), FONT)
    for button in radio_buttons:
        button.draw(screen)
    message_box.draw(screen)
    for button in buttons:
        draw_button(screen, button['rect'], button['color'], button['text'], FONT)
    pygame.display.flip()


message_box = MessageBox((50, 330, 700, 50))
# Main loop
def OpenSignUpPage():
    """
    Displays the sign-up screen and handles user interaction for account creation.
    """
    pygame.init()
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sign Up / Sign In")

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
                message_box.text = "Sign Up Successful"
                # Clear the screen
                screen.fill(WHITE)
                pygame.display.flip()

                # Display "Sign Up Successful" message
                draw_text(screen, "Sign Up Successful", BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                          FONT_TITLE)
                pygame.display.flip()

                # Wait for 3 seconds
                time.sleep(3)

                SignInPage.OpenSignInPage()




        

    def go_back():
        return 'back'


    buttons_sign_up = [
        {'rect': pygame.Rect(200, 380, 200, 50), 'color': GRAY, 'text': "Sign Up", 'action': sign_up},
        {'rect': pygame.Rect(10, 10, 100, 50), 'color': GRAY, 'text': "Back", 'action': go_back}
    ]

    while True:
        events = pygame.event.get()
        handle_input(events, text_boxes, buttons_sign_up)
        sign_up_screen(text_boxes, buttons_sign_up, radio_buttons, screen)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_sign_up:
                    if button['rect'].collidepoint(event.pos):
                        action = button['action']()
                        if action == 'back':
                            return 'back'

            # Handle events for radio buttons
            for button in radio_buttons:
                button.handle_event(event)

        pygame.display.update()

if __name__ == "__main__":
    OpenSignUpPage()
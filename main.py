import pygame
import sys
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

# Fonts
FONT = pygame.font.Font(None, 32)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sign Up / Sign In")

# Textbox class
class TextBox:
    """
    Represents a textbox for text input in Pygame.

    Attributes:
        rect (pygame.Rect): The rectangle defining the textbox position and size.
        color (tuple): The color of the textbox (RGB).
        text (str): The current text content of the textbox.
        txt_surface (pygame.Surface): The surface to render text on.
        active (bool): The state of the textbox, active or not.

    Methods:
        handle_event: Process events related to the textbox, such as typing or clicking.<br>
        draw: Render the textbox on the screen.<br>
        get_text: Return the current text content.
    """
    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.color = BLACK
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
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
        pygame.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text
# Function to draw text on the screen
def draw_text(surface, text, color, rect, font):
    """
    Draws text on the Pygame surface at the specified location.

    Parameters:
        surface (pygame.Surface): The Pygame surface to draw on.
        text (str): The text to draw.
        color (tuple): The color of the text (RGB).
        rect (pygame.Rect): The rectangle defining the position to draw the text.
        font (pygame.Font): The font to use for rendering the text.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = rect.center
    surface.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(surface, rect, color, text, font):
    """
    Draws a button on the Pygame surface.
    
    Parameters:
        surface (pygame.Surface): The surface to draw the button onto.
        rect (pygame.Rect): The rectangle that defines the button's size and position.
        color (tuple): The color of the button.
        text (str): The label text of the button.
        font (pygame.Font): The font used for the button's text.
    """
    pygame.draw.rect(surface, color, rect)
    draw_text(surface, text, BLACK, rect, font)

# Function to handle input events
def handle_input(events, text_boxes, buttons):
    """
    Handles all input events for text boxes and button interactions.
    
    Parameters:
        events (list): A list of events fetched from pygame.event.get().
        text_boxes (list): A list of TextBox instances to be checked for events.
        buttons (list): A list of dicts with button properties and actions to be checked for events.
    """
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
    A class representing a radio button for option selection.
    
    Attributes:
        rect (pygame.Rect): Defines the position and dimensions of the radio button.
        color (tuple): The color of the radio button.
        text (str): The label text of the radio button.
        font (pygame.Font): The font used for the radio button's text.
        selected (bool): State of the radio button, True if it is selected.
        
    Methods:
        handle_event: Responds to events, updating the selected state based on user interaction.<br>
        draw: Renders the radio button and its label onto the screen.<br>
        is_selected: Returns the selected state of the radio button.<br>
        getText: Returns the label text of the radio button.
    """
    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.color = BLACK
        self.text = text
        self.font = FONT
        self.selected = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = True
            else:
                self.selected = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        if self.selected:
            pygame.draw.circle(surface, self.color, (self.rect.x + 10, self.rect.y + 10), 6)

        # Calculate text position to center it within the button
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect.topleft)

    def is_selected(self):
        return self.selected

    def getText(self):
        return self.text

class MessageBox:
    """
    A class representing a message box for displaying notifications and messages.
    
    Attributes:
        rect (pygame.Rect): Defines the position and dimensions of the message box.
        color (tuple): The background color of the message box.
        text (str): The message text to be displayed in the message box.
        
    Methods:
        draw: Renders the message box and its content onto the screen.
    """
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.color = WHITE
        self.text = ""

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text:
            draw_text(surface, self.text,(255,0,0), self.rect, FONT)

# Function to display sign up screen
FONT_TITLE = pygame.font.Font(None, 48)
def sign_up_screen(text_boxes, buttons, radio_buttons):
    """
    Renders the sign-up screen interface.

    Parameters:
        text_boxes (list): A list of TextBox objects for user input.
        buttons (list): A list of dictionaries, each describing a button with properties like rectangle, color, text, and action.
        radio_buttons (list): A list of RadioButton objects for choosing user roles.
        screen (pygame.Surface): The surface to draw the sign-up interface elements onto.

    This function renders a title, multiple input fields for username, password, and email,
    as well as options to choose a user role. It also displays buttons for submitting the sign-up form or navigating to the sign-in screen.
    """
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
# Function to display sign in screen
def sign_in_screen(text_boxes, buttons):
    """
    Renders the sign-in screen interface.

    Parameters:
        text_boxes (list): A list of TextBox objects for username and password input.
        buttons (list): A list of dictionaries, each describing a button with properties like rectangle, color, text, and action.
        screen (pygame.Surface): The surface to draw the sign-in interface elements onto.

    This function renders a title and input fields for the username and password.
    It also provides a sign-in button and a navigation option to go to the sign-up screen.
    """
    screen.fill(WHITE)
    # Draw the title "Number Ninjas"
    draw_text(screen, "Number Ninjas", BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, 100), FONT_TITLE)
    # Draw input fields for username, password
    draw_text(screen, "Sign In", BLACK, pygame.Rect(0, 75, SCREEN_WIDTH, 50), FONT)
    draw_text(screen, "Username:", BLACK, pygame.Rect(50, 120, 200, 30), FONT)
    text_boxes[0].draw(screen)
    draw_text(screen, "Password:", BLACK, pygame.Rect(50, 170, 200, 30), FONT)
    text_boxes[1].draw(screen)
    message_box.draw(screen)
    for button in buttons:
        draw_button(screen, button['rect'], button['color'], button['text'], FONT)
    pygame.display.flip()

# Main loop
def main():
    """
    The main function orchestrates the user authentication process for the Number Ninjas game.

    It initializes and displays either the sign-up or sign-in screen, allowing new players to create an account or existing players to log in with their credentials. The function enters a loop that continuously listens for user input and renders the appropriate UI elements on the screen. The loop runs indefinitely, updating the display in response to the user's actions, until the user chooses to exit the game or switch between sign-in and sign-up screens.
    
    Attributes:
        text_boxes (list): Collection of TextBox instances for entering user information.
        buttons_sign_up (list): Collection of button dictionaries for the sign-up screen actions.
        buttons_sign_in (list): Collection of button dictionaries for the sign-in screen actions.
        current_screen (function): The function representing the current screen displayed to the user.
    """
    username_box = TextBox((250, 120, 300, 30))
    password_box = TextBox((250, 170, 300, 30))
    email_box = TextBox((250, 220, 300, 30))
    text_boxes = [username_box, password_box, email_box]

    # Radio buttons initialization
    student_button = RadioButton((250, 280, 150, 30), "Student")
    teacher_button = RadioButton((400, 280, 150, 30), "Teacher")
    moderator_button = RadioButton((550, 280, 150, 30), "Moderator")
    radio_buttons = [student_button, teacher_button, moderator_button]

    def go_to_sign_in():
        nonlocal current_screen
        current_screen = sign_in_screen

    def go_to_sign_up():
        nonlocal current_screen
        current_screen = sign_up_screen

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
            message_box.text="Missing fields required."
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

    def sign_in():
        username = username_box.get_text()
        password = password_box.get_text()
        saves = savedata()
        userData = saves.getUserData(username, password)
        if userData == None:
            message_box.text = "Invalid username or password."
        else:
            usertype = userData['User_Type']
            if usertype == 'Student':
                user = Student()
            elif usertype == 'Teacher':
                user = Teacher()
            else:
                user = Admin()

            user.signin(userData['Username'], userData['Password'], saves)
            print(user.email)

    buttons_sign_up = [
        {'rect': pygame.Rect(200, 380, 200, 50), 'color': GRAY, 'text': "Sign Up", 'action': sign_up},
        {'rect': pygame.Rect(200, 440, 200, 50), 'color': GRAY, 'text': "Go to Sign In", 'action': go_to_sign_in}
    ]

    buttons_sign_in = [
        {'rect': pygame.Rect(200, 380, 200, 50), 'color': GRAY, 'text': "Sign In", 'action': sign_in},
        {'rect': pygame.Rect(200, 440, 200, 50), 'color': GRAY, 'text': "Go to Sign Up", 'action': go_to_sign_up}
    ]
    current_screen = sign_up_screen  # Start with sign up screen
    while True:
        events = pygame.event.get()
        handle_input(events, text_boxes, buttons_sign_up if current_screen == sign_up_screen else buttons_sign_in)
        if current_screen == sign_up_screen:
            current_screen(text_boxes, buttons_sign_up, radio_buttons)
            if events:  # Check if events list is not empty
                for button in radio_buttons:
                    button.handle_event(events[0])  # Assuming only one event is handled at a time
        else:
            current_screen(text_boxes, buttons_sign_in)  # Pass only necessary arguments
        pygame.display.update()


if __name__ == "__main__":
    main()





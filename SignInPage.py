import pygame
import sys
from savedata import savedata
from Student import Student
from Teacher import Teacher
from Admin import Admin
from UserScreen import user_menu
from TeacherMode import TeacherMode
from MainGamePageAdmin import adminPage

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



# Textbox class
class TextBox:
    """
    A class for creating interactive text boxes in Pygame.

    Attributes:
        rect (pygame.Rect): The rectangle defining the textbox's position and size.
        text (str): The text content of the textbox.
        txt_surface (pygame.Surface): The surface used to display the text.
        active (bool): Indicates whether the textbox is active (selected).
    """
    def __init__(self, rect, text=''):
        """
        Initializes the TextBox with a rectangle and optional default text.
        """
        self.rect = pygame.Rect(rect)
        self.color = BLACK
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        Handles events related to the textbox, such as typing and selecting.
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
        Draws the textbox and its current text on a Pygame surface.
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
    """
    Draws text on a Pygame surface within a given rectangle.

    Parameters:
        surface (pygame.Surface): The surface to draw on.
        text (str): The text to draw.
        color (tuple): The color of the text.
        rect (pygame.Rect): The rectangle to draw the text in.
        font (pygame.font.Font): The font to use for the text.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = rect.center
    surface.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(surface, rect, color, text, font):
    """
    Draws a button with text on a Pygame surface.

    Parameters:
        surface (pygame.Surface): The surface to draw on.
        rect (pygame.Rect): The rectangle defining the button's position and size.
        color (tuple): The color of the button.
        text (str): The text to display on the button.
        font (pygame.font.Font): The font to use for the text.
    """
    pygame.draw.rect(surface, color, rect)
    draw_text(surface, text, BLACK, rect, font)

# Function to handle input events
def handle_input(events, text_boxes, buttons):
    """
    Handles input events for text boxes and buttons.

    Parameters:
        events (list): A list of Pygame events to handle.
        text_boxes (list): A list of TextBox objects to process.
        buttons (list): A list of dictionaries defining buttons and their actions.
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
    A class for creating radio buttons in Pygame.

    Attributes:
        rect (pygame.Rect): The rectangle defining the button's position and size.
        text (str): The text label of the radio button.
        selected (bool): Indicates whether the radio button is selected.
    """
    def __init__(self, rect, text=''):
        """
        Initializes the RadioButton with a rectangle and optional label text.
        """
        self.rect = pygame.Rect(rect)
        self.color = BLACK
        self.text = text
        self.font = FONT
        self.selected = False

    def handle_event(self, event):
        """
        Handles events related to the radio button, such as selecting.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = True
            else:
                self.selected = False

    def draw(self, surface):
        """
        Draws the radio button and its label on a Pygame surface.
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
        Returns True if the radio button is selected, False otherwise.
        """
        return self.selected

    def getText(self):
        """
        Returns the label text of the radio button.
        """
        return self.text

class MessageBox:
    """
    A class for creating message boxes in Pygame to display text messages.

    Attributes:
        rect (pygame.Rect): The rectangle defining the message box's position and size.
        text (str): The message text to display.
    """
    def __init__(self, rect):
        """
        Initializes the MessageBox with a rectangle.
        """
        self.rect = pygame.Rect(rect)
        self.color = WHITE
        self.text = ""

    def draw(self, surface):
        """
        Draws the message box and its text on a Pygame surface.
        """
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text:
            draw_text(surface, self.text,(255,0,0), self.rect, FONT)

# Function to display sign up screen
FONT_TITLE = pygame.font.Font(None, 48)



message_box = MessageBox((50, 330, 700, 50))
# Function to display sign in screen
def sign_in_screen(text_boxes, buttons,screen):
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
def OpenSignInPage():
    """
    The main function to display the sign-in screen and handle user interaction.
    """
    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sign In")

    username_box = TextBox((250, 120, 300, 30))
    password_box = TextBox((250, 170, 300, 30))
    text_boxes = [username_box, password_box]

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
                user.signin(userData['Username'], userData['Password'], saves)
                user_menu(user)
            elif usertype == 'Teacher':
                user = Teacher()
                user.signin(userData['Username'], userData['Password'], saves)
                TeacherMode()
            else:
                user = Admin()
                user.signin(userData['Username'], userData['Password'], saves)
                adminPage()


            print(user.email)

    def go_back():
        return 'back'

    buttons_sign_in =[
            {'rect': pygame.Rect(200, 380, 200, 50), 'color': GRAY, 'text': "Sign In", 'action': sign_in},
            {'rect': pygame.Rect(10, 10, 100, 50), 'color': GRAY, 'text': "Back", 'action': go_back}
            ]

    while True:
        events = pygame.event.get()
        handle_input(events, text_boxes, buttons_sign_in)
        sign_in_screen(text_boxes, buttons_sign_in,screen)
        pygame.display.update()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_sign_in:
                    if button['rect'].collidepoint(event.pos):
                        action = button['action']()
                        if action == 'back':
                            return 'back'


if __name__ == "__main__":
    OpenSignInPage()
import pygame
import sys
from Student import Student

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Progress")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Font initialization
FONT = pygame.font.Font(None, 32)
FONT_LARGE = pygame.font.Font(None, 48)

# Function to draw the level boxes, paths, and level numbers
def draw_levels(student_score, total_levels=10):
    """
    Draws the level boxes and their connecting paths based on the student's progress.

    Parameters:
    - student_score (int): The current score of the student, determining how many levels have been cleared.
    - total_levels (int, optional): The total number of levels available in the game.
    """
    offset_x, offset_y = 140, 70
    box_size = 50
    # Set starting positions and offset
    start_x, start_y = WIDTH // 2 - 2 * (offset_x // 2), HEIGHT // 2 - (5 // 2) * offset_y


    # Draw level boxes and paths
    for level in range(total_levels):
        x = start_x + (level % 2) * offset_x  # Alternate x position
        y = start_y + (level // 2) * offset_y  # Move down after every two levels

        color = GREEN if level < student_score else WHITE
        box_rect = pygame.Rect(x - box_size // 2, y - box_size // 2, box_size, box_size)
        pygame.draw.rect(screen, color, box_rect)

        level_text = FONT.render(str(level + 1), True, BLACK)
        level_text_rect = level_text.get_rect(center=box_rect.center)
        screen.blit(level_text, level_text_rect)

        if level < student_score:
            draw_crossed_box(x, y, box_size)

        if level < total_levels - 1:  # Draw paths between levels except the last one
            next_x = start_x + ((level + 1) % 2) * offset_x
            next_y = start_y + ((level + 1) // 2) * offset_y
            pygame.draw.line(screen, GRAY, (x, y), (next_x, next_y), 5)

# Function to draw a crossed box
def draw_crossed_box(center_x, center_y, size):
    """
    Draws a crossed box at the specified location, indicating a cleared level.

    Parameters:
    - center_x (int): The X coordinate of the box's center.
    - center_y (int): The Y coordinate of the box's center.
    - size (int): The size of the box.
    """
    pygame.draw.line(screen, BLACK, (center_x - size // 2, center_y - size // 2),
                     (center_x + size // 2, center_y + size // 2), 3)
    pygame.draw.line(screen, BLACK, (center_x + size // 2, center_y - size // 2),
                     (center_x - size // 2, center_y + size // 2), 3)

# Function to draw the progress screen
def draw_progress_screen(student):
    """
    Draws the entire progress screen, including the level boxes, current level, questions solved, and back button.

    Parameters:
    - student (Student): The student object, containing their current score and level.
    """
    screen.fill(WHITE)

    # Draw the Ninja Map title
    ninja_map_text = FONT_LARGE.render("Ninja Map", True, BLACK)
    ninja_map_rect = ninja_map_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(ninja_map_text, ninja_map_rect)

    # Draw the levels
    draw_levels(student.getScore())

    # Display the current level and questions solved
    current_level = student.getScore() + 1
    questions_solved = student.getScore() * 5  # This assumes each level has 5 questions
    if current_level<=10:
        current_level_text = FONT.render(f"Current Level: {current_level}", True, BLACK)
    else:
        current_level_text = FONT.render(f"Current Level: Complete!", True, BLACK)
    current_level_rect = current_level_text.get_rect(center=(WIDTH // 2, HEIGHT - 70))
    screen.blit(current_level_text, current_level_rect)

    questions_solved_text = FONT.render(f"Questions Solved: {questions_solved}", True, BLACK)
    questions_solved_rect = questions_solved_text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
    screen.blit(questions_solved_text, questions_solved_rect)

    # Draw the back button on the bottom right
    back_button = FONT.render("Back", True, BLACK)
    back_button_rect = back_button.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
    pygame.draw.rect(screen, GRAY, back_button_rect.inflate(20, 10))
    screen.blit(back_button, back_button_rect)

    pygame.display.update()

    return back_button_rect  # Return the rect for event handling

# Main loop for the progress screen
def progress_main(student):
    """
    The main loop for the progress screen, handling events and updating the display.

    Parameters:
    - student (Student): The student object, used to draw the progress screen.
    """
    running = True
    back_button_rect = draw_progress_screen(student)  # Draw the screen once and get the back button rect

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    running = False  # Go back to the previous menu

if __name__ == "__main__":
    # You need to pass a student object here. For testing, we'll create a mock student class
    class MockStudent:
        def __init__(self, score):
            self.score = score
        def getScore(self):
            return self.score
    # Pass a student object with a score indicating the progress
    student = MockStudent(score=3)  # Replace 3 with the actual score
    progress_main(student)

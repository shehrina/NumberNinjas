import pygame
from MathQuestion import MathQuestion
from Enemy import Enemy
from Room import Room
import random
import sys


def generate_questions(difficulty, num_questions):
    """
    Parameters:
        difficulty(int): The level of difficulty for the questions.
        num_questions(int): The number of questions to generate.

    Returns:
        List[Enemy]: A list of enemies, each associated with a math question.
    """
    questions = []
    for i in range(num_questions):
        operation = random.choice(['+', '-']) if difficulty <= 5 else random.choice(['*', '/'])
        question = MathQuestion(difficulty)
        if difficulty == 1:
            question.generate_question(operation, 0, 10)
        elif difficulty == 2:
            question.generate_question(operation, 10, 30)
        elif difficulty == 3:
            question.generate_question(operation, 10, 50)
        elif difficulty == 4:
            question.generate_question(operation, 10, 80)
        elif difficulty == 5:
            question.generate_question(operation, 10, 100)
        else:
            question.generate_question(operation, 0, 10)
        enemy = Enemy(question, False)
        questions.append(enemy)
    return questions

def adminPage():
    """
    Main function for running the NumberNinja game. Initializes the game, creates rooms with questions,
    and manages the game loop including rendering the UI, handling user inputs, and navigating between game states.

    The function sets up the Pygame window, loads assets, and then enters a game loop where it updates the game
    state and renders the UI based on the current game state. It supports typing answers, navigating between questions
    and levels, and provides feedback on user answers. The game progresses through different rooms, each with its own
    set of math questions and associated enemies. It includes features for skipping levels and exiting the game.
    """
    screen = pygame.display.set_mode((800, 600))
    pygame.init()
    screen_width, screen_height = 800, 600
    window_surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Number Ninjas')
    background_image = pygame.image.load('assets/gamebackground.png')
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    LIGHT_GRAY = (150, 150, 150)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    background_color = pygame.Color('#FFFFFF')

    text_box_rect = pygame.Rect(350, 275, 100, 50)
    submit_button_rect = pygame.Rect(350, 335, 100, 50)

    # New text box and button for skipping levels
    skip_level_text_box_rect = pygame.Rect(600, 500, 50, 30)
    skip_button_rect = pygame.Rect(670, 500, 70, 30)

    text = ""
    skip_text = ""

    is_typing = False
    skip_typing = False

    current_difficulty = 1
    num_questions_per_room = 5
    rooms = []

    for i in range(10):
        room_difficulty = current_difficulty + i
        questions = generate_questions(room_difficulty, num_questions_per_room)
        room = Room(room_difficulty)
        room.questions = questions
        rooms.append(room)

    current_room_index = 0
    current_room = rooms[current_room_index]

    is_running = True
    previous_room_index = current_room_index
    feedback_text = None
    invalid_room_text = None

    while is_running:
        window_surface.fill(background_color)
        screen.blit(background_image, (0, 0))
        ninja_image = pygame.image.load('assets/Ninja.png')
        if current_room_index == 0:
            enemy_image = pygame.image.load('assets/enemy1.png')
        elif current_room_index == 1:
            enemy_image = pygame.image.load('assets/enemy2.png')
        elif current_room_index == 2:
            enemy_image = pygame.image.load('assets/enemy3.png')
        elif current_room_index == 3:
            enemy_image = pygame.image.load('assets/enemy4.png')
        elif current_room_index == 4:
            enemy_image = pygame.image.load('assets/enemy5.png')
        elif current_room_index == 5:
            enemy_image = pygame.image.load('assets/enemy6.png')
        elif current_room_index == 6:
            enemy_image = pygame.image.load('assets/enemy7.png')
        elif current_room_index == 7:
            enemy_image = pygame.image.load('assets/enemy8.png')
        elif current_room_index == 8:
            enemy_image = pygame.image.load('assets/enemy9.png')
        else:
            enemy_image = pygame.image.load('assets/enemy10.png')
        ninja_image = pygame.transform.scale(ninja_image, (300, 400))
        enemy_image = pygame.transform.scale(enemy_image, (300, 300))
        ninja_rect = ninja_image.get_rect(left=-40, bottom=screen_height - 50)
        enemy_rect = enemy_image.get_rect(right=screen_width + 30, centery=screen_height // 2)
        screen.blit(ninja_image, ninja_rect)
        screen.blit(enemy_image, enemy_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box_rect.collidepoint(event.pos):
                    is_typing = True
                else:
                    is_typing = False
                if skip_level_text_box_rect.collidepoint(event.pos):
                    skip_typing = True
                else:
                    skip_typing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_box_rect.collidepoint(event.pos):
                        is_typing = True
                    else:
                        is_typing = False
                    if skip_level_text_box_rect.collidepoint(event.pos):
                        skip_typing = True
                    else:
                        skip_typing = False
                    if submit_button_rect.collidepoint(event.pos):
                        current_question = current_room.questions[current_room.current_question_index].equation
                        user_answer = int(text) if text.isdigit() else None
                        if user_answer is not None:
                            if user_answer == current_question.answer:
                                feedback_text = font.render(current_question.check_answer(user_answer), True, GREEN)
                                feedback_start_time = pygame.time.get_ticks()
                                current_room.current_question_index += 1
                                if current_room.current_question_index >= len(current_room.questions):
                                    current_room_index += 1
                                    if current_room_index < len(rooms):
                                        current_room = rooms[current_room_index]
                                    else:
                                        is_running = False
                            else:
                                feedback_text = font.render(current_question.check_answer(user_answer), True, RED)
                                feedback_start_time = pygame.time.get_ticks()
                        text = ""
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if back_button_rect.collidepoint(event.pos):
                            return
                    if skip_button_rect.collidepoint(event.pos):
                        skip_level = int(skip_text) if skip_text.isdigit() else None
                        if skip_level is not None and 1 <= skip_level <= 10:
                            current_room_index = skip_level - 1
                            current_room = rooms[current_room_index]
                            skip_text = ""
                        else:
                            invalid_room_text = font.render("Invalid Room Number", True, RED)

            if event.type == pygame.KEYDOWN and is_typing:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(text)
                    text = ""
                else:
                    text += event.unicode

            if event.type == pygame.KEYDOWN and skip_typing:
                if event.key == pygame.K_BACKSPACE:
                    skip_text = skip_text[:-1]
                else:
                    skip_text += event.unicode

        if current_room_index <= 9:
            current_question = current_room.questions[current_room.current_question_index].equation
        else:
            window_surface.fill(background_color)
            pygame.display.update()

        if current_room_index == 10:
            congratulations_text = font.render("Congratulations, you have cleared Number Ninjas!!!", True, BLACK)
            congratulations_rect = congratulations_text.get_rect(center=(screen_width // 2, screen_height // 2))
            window_surface.blit(congratulations_text, congratulations_rect)
            pygame.display.update()
            pygame.time.wait(5000)  # Display the message for 5 seconds
            pygame.display.update()
            is_running = False
            break

        question_text = font.render(current_question.get_question(), True, pygame.Color('#000000'))
        question_rect = question_text.get_rect(center=(400, 200))
        question_box_rect = pygame.Rect(question_rect.left - 10, question_rect.top - 10, question_rect.width + 20,
                                        question_rect.height + 20)
        pygame.draw.rect(window_surface, WHITE, question_box_rect)  # Draw white box
        window_surface.blit(question_text, question_rect)

        pygame.draw.rect(window_surface, WHITE, text_box_rect)
        if is_typing:
            pygame.draw.rect(window_surface, BLACK, text_box_rect, 2)
        else:
            pygame.draw.rect(window_surface, GREY, text_box_rect, 2)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=text_box_rect.center)
        window_surface.blit(text_surface, text_rect)

        pygame.draw.rect(window_surface, WHITE, submit_button_rect)
        pygame.draw.rect(window_surface, BLACK, submit_button_rect, 2)
        submit_text = font.render("Submit", True, BLACK)
        submit_text_rect = submit_text.get_rect(center=submit_button_rect.center)
        window_surface.blit(submit_text, submit_text_rect)

        # Draw skip level text box and button
        pygame.draw.rect(window_surface, WHITE, skip_level_text_box_rect)
        pygame.draw.rect(window_surface, BLACK, skip_level_text_box_rect, 2)
        skip_level_text = font.render(skip_text, True, BLACK)
        skip_level_text_rect = skip_level_text.get_rect(center=skip_level_text_box_rect.center)
        window_surface.blit(skip_level_text, skip_level_text_rect)

        pygame.draw.rect(window_surface, WHITE, skip_button_rect)
        pygame.draw.rect(window_surface, BLACK, skip_button_rect, 2)
        skip_button_text = font.render("Skip", True, BLACK)
        skip_button_text_rect = skip_button_text.get_rect(center=skip_button_rect.center)
        window_surface.blit(skip_button_text, skip_button_text_rect)

        # Add this section to create and render the back button
        back_button_rect = pygame.Rect(10, 10, 100, 50)
        pygame.draw.rect(window_surface, BLACK, back_button_rect, border_radius=10)
        pygame.draw.rect(window_surface, LIGHT_GRAY, back_button_rect)
        back_text = font.render('Back', True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        window_surface.blit(back_text, back_text_rect)

        level_text = font.render(f"Level: {current_room_index + 1}", True, BLACK)
        level_rect = level_text.get_rect(topright=(screen_width - 10, 10))
        window_surface.blit(level_text, level_rect)

        # Display "Level completed" message when the level changes
        if current_room_index > 0 and current_room_index != previous_room_index:
            level_completed_text = font.render("Level Cleared!", True, GREEN)
            level_completed_rect = level_completed_text.get_rect(center=(screen_width // 2, 100))
            window_surface.blit(level_completed_text, level_completed_rect)
            pygame.display.update()
            pygame.time.wait(3000)  # Display the message for 3 seconds
            previous_room_index = current_room_index

        if feedback_text is not None:
            if pygame.time.get_ticks() - feedback_start_time < 1000:
                feedback_rect = feedback_text.get_rect(center=(screen_width // 2, 50))
                window_surface.blit(feedback_text, feedback_rect)
            else:
                feedback_text = None

        if invalid_room_text is not None:
            invalid_room_rect = invalid_room_text.get_rect(center=(screen_width // 2, 550))
            window_surface.blit(invalid_room_text, invalid_room_rect)
            pygame.display.update()
            pygame.time.wait(2000)
            invalid_room_text = None

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    adminPage()

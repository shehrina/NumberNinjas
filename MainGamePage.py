import pygame
from MathQuestion import MathQuestion
from Enemy import Enemy
from Room import Room
from savedata import savedata
import random
import sys

def generate_questions(difficulty, num_questions):
    """
    Generates a list of math question enemies based on the specified difficulty and number of questions.
    
    This function utilizes randomness and conditional logic to craft a series of math problems tailored to the player's current level, represented by the difficulty parameter. Each question is associated with an Enemy object, signifying a challenge the player must overcome.

    Parameters:
        difficulty (int): A numerical value representing the game's current difficulty level. Higher values indicate more complex math operations and larger number ranges.
        num_questions (int): The total number of math question enemies to generate for the current game session or level.
    
    Returns:
        list: A list of Enemy objects, each encapsulating a math question generated based on the specified difficulty. 

    The function showcases several programming concepts:
    - **Randomness**: Employed to select math operations and generate number ranges, ensuring a variety of questions.
    - **Conditional Logic**: Adjusts the complexity of math operations and the range of numbers used in questions according to the difficulty level.
    - **Object-Oriented Programming**: Each math question is encapsulated within an Enemy object, demonstrating the use of classes to organize and manage related data and behaviors.

    Example:
        >>> generate_questions(3, 5)
        [Enemy(MathQuestion('What is 15 + 6?'), False), ...]
    
    Note:
    This function is central to the adaptive challenge system of the game, dynamically adjusting the gameplay to match the player's progression and skill level.
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

def gamePage(user):
    """
    🌠 The Grand Arena of Number Ninjas 🌠

    Welcome to the digital dojo where every math problem is a battle, and each correct answer is a victorious strike against the numerically embodied foes. Here's where our brave player, donning the virtual ninja garb, embarks on a quest of wit, speed, and arithmetic prowess.

    🎮 Gameplay Experience:
    - Players face a series of math challenges, each tailored to their current level of mastery.
    - Correct answers allow the player to progress, slicing through mathematical confusion like a sharp katana through bamboo.
    - The game's backdrop, enemies, and feedback are all rendered in vibrant detail, immersing the player in a world where numbers rule.

    Parameters:
        user (Player): An object representing the player, including their current score and progression within the game. This parameter is crucial for tailoring the game experience to the player's level.
    
    Key Concepts:
    - **Pygame Library**: Utilizes Pygame for creating a game window, handling events, and rendering graphics.
    - **Game Loop**: Implements a continuous loop where game state is updated and graphics are rendered in real-time based on player interactions.
    - **Event Handling**: Processes user input through mouse clicks and keyboard presses to interact with the game elements.
    - **Conditional Rendering**: Displays different enemies and feedback based on the player's current level and answers to questions.
    - **Object-Oriented Design**: Leverages classes such as Enemy and Room to organize game data and logic.
    
    The function integrates several aspects of game development, from graphical rendering and event handling to the use of data structures for managing game state. By dynamically adjusting the challenges presented to the player, it exemplifies adaptive difficulty in educational games.

    Example Usage:
    Assume 'servos' is an instance of a Player class with necessary attributes:
        >>> gamePage(servos)
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

    text = ""
    is_typing = False

    current_difficulty = 1
    num_questions_per_room = 5
    rooms = []

    for i in range(10):
        room_difficulty = current_difficulty + i
        questions = generate_questions(room_difficulty, num_questions_per_room)
        room = Room(room_difficulty)
        room.questions = questions
        rooms.append(room)

    current_room_index = user.getScore()
    if current_room_index < 10:
        current_room = rooms[current_room_index]

    is_running = True
    previous_room_index = current_room_index
    feedback_text = None

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_box_rect.collidepoint(event.pos):
                        is_typing = True
                    else:
                        is_typing = False
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
                                    user.nextLevel()
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
                            data = savedata()
                            data.saveGame(user)
                            return
            if event.type == pygame.KEYDOWN and is_typing:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(text)
                    text = ""
                else:
                    text += event.unicode

        if current_room_index <= 9:
            current_question = current_room.questions[current_room.current_question_index].equation
        else:
            window_surface.fill(background_color)
            pygame.display.update()

        if current_room_index >= 10:
            congratulations_text = font.render("Congratulations, you have cleared Number Ninjas!!!", True, BLACK)
            congratulations_rect = congratulations_text.get_rect(center=(screen_width // 2, screen_height // 2))
            window_surface.blit(congratulations_text, congratulations_rect)
            pygame.display.update()
            data = savedata()
            data.saveGame(user)
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

        # Add this section to create and render the back button
        back_button_rect = pygame.Rect(10, 10, 100, 50)
        pygame.draw.rect(window_surface, BLACK, back_button_rect, border_radius=10)
        pygame.draw.rect(window_surface, LIGHT_GRAY, back_button_rect)
        back_text = font.render('Back', True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        window_surface.blit(back_text, back_text_rect)

        level_text = font.render(f"Level: {current_room_index+1}", True, BLACK)
        level_rect = level_text.get_rect(topright=(screen_width - 10, 10))
        window_surface.blit(level_text, level_rect)

        # Display "Level completed" message when the level changes
        if current_room_index > 0 and current_room_index != previous_room_index:
            level_completed_text = font.render("Level Cleared!", True, GREEN)
            level_completed_rect = level_completed_text.get_rect(center=(screen_width // 2, 100))
            window_surface.blit(level_completed_text, level_completed_rect)
            pygame.display.update()
            pygame.time.wait(3000)  # Display the message for 3 second
            previous_room_index = current_room_index

        if feedback_text is not None:
            if pygame.time.get_ticks() - feedback_start_time < 1000:
                feedback_rect = feedback_text.get_rect(center=(screen_width // 2, 50))
                window_surface.blit(feedback_text, feedback_rect)
            else:
                feedback_text = None

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    gamePage(super)

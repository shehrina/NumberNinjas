import pygame
from MathQuestion import MathQuestion
from Enemy import Enemy
from Room import Room
import random
import sys

screen = pygame.display.set_mode((800, 600))
def generate_questions(difficulty, num_questions):
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


def main(screen):
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

    current_room_index = 0
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


        # Define text parameters
        text_color = (255, 255, 0)
        text_font = pygame.font.Font(None, 30)

        # Define text messages
        text_messages = [
            "Review the question given!"
            " ",
            "Type your answer in the box! -->",
            "<-- Submit to move on!",
            "Receive feedback on each answer above!",
        ]

        text_positions = [
            (400, 150),
            (30, 300),
            (470, 350),
            (150, 70),
            (150, 500)
        ]

        for message, position in zip(text_messages, text_positions):
            text_render = text_font.render(message, True, text_color)
            text_rect = text_render.get_rect(topleft=position)
            window_surface.blit(text_render, text_rect)

        text_color = (255, 255, 0)
        text_font = pygame.font.Font(None, 30)

        text_messagess = [
            "Keep practicing until you're ready for a real game!",
        ]

        text_positionss = [
            (150, 500)
        ]

        for message, position in zip(text_messagess, text_positionss):
            text_renders = text_font.render(message, True, text_color)
            text_rects = text_render.get_rect(topleft=position)
            window_surface.blit(text_renders, text_rects)
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    print("Back button clicked")
                    return 'back'
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
                            if current_room.current_question_index >= 5:
                                current_room.current_question_index = 1
                            if current_room.current_question_index >= len(current_room.questions):
                                if current_room_index < len(rooms):
                                    current_room = rooms[current_room_index]
                                else:
                                    is_running = False
                        else:
                            feedback_text = font.render(current_question.check_answer(user_answer), True, RED)
                            feedback_start_time = pygame.time.get_ticks()
                        text = ""
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


        if current_room_index == 10:
            congratulations_text = font.render("Congratulations, you have cleared Number Ninjas!", True, BLACK)
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

        # Add this section to create and render the back button
        back_button_rect = pygame.Rect(10, 10, 100, 50)
        pygame.draw.rect(window_surface, BLACK, back_button_rect, border_radius=10)
        pygame.draw.rect(window_surface, LIGHT_GRAY, back_button_rect)
        back_text = font.render('Back', True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        window_surface.blit(back_text, back_text_rect)

        level_text = font.render("Tutorial", True, BLACK)
        level_rect = level_text.get_rect(topright=(screen_width - 10, 10))
        window_surface.blit(level_text, level_rect)

        if current_room_index > 0 and current_room_index != previous_room_index:
            level_completed_text = font.render("Tutorial level completed! Think you're ready yet?", True, (255, 0, 255))
            level_completed_rect = level_completed_text.get_rect(center=(screen_width // 2, 100))
            window_surface.blit(level_completed_text, level_completed_rect)
            pygame.display.update()
            pygame.time.wait(10000) 
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
    main(screen)

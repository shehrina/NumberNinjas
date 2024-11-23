import pygame
import sys
import pandas as pd
from savedata import savedata

# Function to display DataFrame in teacher mode
def TeacherMode():
    try:
        # Define colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GRAY = (200, 200, 200)

        # Initialize Pygame
        pygame.init()

        # Set up the display
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Number Ninjas: Teacher/Instructor Mode")  # Set the title
        running = True
        x, y = 50, 50

        df = savedata()
        df = df.getDataframe()
        df = df[df['User_Type'] == 'Student']

        # Remove 'User_Type' column
        df = df.drop(columns=['User_Type'])

        # Define button dimensions and position
        button_width = 100
        button_height = 40
        button_x = screen_width - button_width - 20
        button_y = screen_height - button_height - 20

        # Scroll parameters
        scroll_speed = 30
        scroll_offset = 0

        # Calculate the maximum scroll offset
        max_visible_rows = (screen_height - y - 100) // 30
        max_scroll = max(len(df) - max_visible_rows, 0)

        # Main loop
        while running:
            screen.fill(WHITE)

            # Display title
            title_font = pygame.font.SysFont(None, 36)
            title_text = title_font.render("Number Ninjas: Teacher/Instructor Mode", True, BLACK)
            screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, 20))

            # Display column headers (excluding 'User_Type' column)
            header_font = pygame.font.SysFont(None, 24)
            columns = df.columns
            for i, col in enumerate(columns):
                text_surface = header_font.render(col, True, BLACK)
                screen.blit(text_surface, (x + i * 150, y))

            # Display data (excluding 'User_Type' column)
            data_font = pygame.font.SysFont(None, 20)
            visible_df = df.iloc[scroll_offset:scroll_offset + max_visible_rows]
            for i, row in enumerate(visible_df.itertuples()):
                for j, value in enumerate(row[1:]):
                    text_surface = data_font.render(str(value), True, BLACK)
                    screen.blit(text_surface, (x + j * 150, y + (i + 1) * 30))

            # Draw exit button
            pygame.draw.rect(screen, GRAY, (button_x, button_y, button_width, button_height))
            button_text = data_font.render("Exit", True, BLACK)
            screen.blit(button_text, (button_x + 20, button_y + 10))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                        running = False
                    elif event.button == 4:  # Scroll up
                        scroll_offset = max(0, scroll_offset - 1)
                    elif event.button == 5:  # Scroll down
                        scroll_offset = min(max_scroll, scroll_offset + 1)

            pygame.display.flip()

    except pygame.error as e:
        print("An error occurred:", e)
    finally:
        pygame.quit()
        sys.exit()







import pygame
from game_function import create_balls, merge_balls_if_collide
from config import Config
from game_state import GameState
from ui_elements import UIManager


def run_game():
    pygame.init()
    # Width and height of the window
    screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Bouncing Balls Entertainment Program")
    clock = pygame.time.Clock()
    game_state = GameState()

    # Variables to keep track of game info
    balls = create_balls(screen, game_state.ball_count)
    clicked_balls = set()
    clicked_balls_count = 0
    offset_x = 0
    offset_y = 0

    running = True
    while running:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # print("mouse button down")
                for ball in balls:
                    if (ball.position[0] - mouse_pos[0]) ** 2 + (ball.position[1] - mouse_pos[1]) ** 2 < ball.radius ** 2:
                        ball.isSelected = True
                        ball.isDragging = True  # You might need to add this attribute to your Ball class
                        offset_x = ball.position[0] - mouse_pos[0]
                        offset_y = ball.position[1] - mouse_pos[1]
                        # print("ball selected")
                        break
            elif event.type == pygame.MOUSEMOTION:
                if any(ball.isDragging for ball in balls):  # Check if any ball is being dragged
                    mouse_pos = event.pos
                    for ball in balls:
                        if ball.isDragging:
                            ball.position[0] = mouse_pos[0] + offset_x
                            ball.position[1] = mouse_pos[1] + offset_y

            elif event.type == pygame.MOUSEBUTTONUP:
                # Deselect all balls when the mouse button is released
                for ball in balls:
                    ball.isSelected = False
                    ball.isDragging = False

        # Clear screen
        screen.fill((255, 255, 255))  # Fill the screen with white

        # Draw the top bar
        # UIManager.draw_top_bar(screen, f"Balls clicked: {clicked_balls_count}")

        for ball in balls:
            ball.attract_others(balls)  # Attract balls of the same color
            ball.move()

        merge_balls_if_collide(screen, balls)

        for ball in balls:
            ball.draw()

        # Update the display to show the next frame
        pygame.display.flip()
        clock.tick(60)

        # Clean up and quit Pygame when the loop is exited
    pygame.quit()


if __name__ == '__main__':
    run_game()

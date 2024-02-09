import pygame
from game_function import create_balls
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
    balls = create_balls(screen, game_state)
    clicked_balls = set()
    clicked_balls_count = 0

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
                        # print("ball selected")
                        ball.radius = 20
                        ball.velocity[0] = 0
                        ball.velocity[1] = 0
                        if ball.id not in clicked_balls:
                            clicked_balls.add(ball.id)
                            clicked_balls_count += 1
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                # Deselect all balls when the mouse button is released
                for ball in balls:
                    ball.isSelected = False

        # Clear screen
        screen.fill((255, 255, 255))  # Fill the screen with white

        # Draw the top bar
        UIManager.draw_top_bar(screen, f"Balls clicked: {clicked_balls_count}")

        for ball in balls:
            ball.move()
            ball.draw()

        # Update the display to show the next frame
        pygame.display.flip()
        clock.tick(60)

        # Clean up and quit Pygame when the loop is exited
    pygame.quit()


if __name__ == '__main__':
    run_game()

import pygame
from game_function import create_balls


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Width and height of the window
    pygame.display.set_caption("Bouncing Balls Entertainment Program")
    clock = pygame.time.Clock()
    running = True
    balls = create_balls(screen, 40)

    while running:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # You can add your game logic and drawing code here
        # For now, let's just fill the screen with a color to see something
        screen.fill((255, 255, 255))  # Fill the screen with white
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

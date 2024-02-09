import pygame
import random
from ball import Ball
from config import Config

BALL_COLORS = [
    (0, 255, 0),  # Green
    (255, 255, 0),  # Yellow
    (0, 0, 255),  # Blue
    (255, 20, 147)  # Pink, using the DeepPink RGB value as an example
]


def get_non_zero_velocity(min_val=-3, max_val=3):
    return random.choice([i for i in range(min_val, max_val + 1) if i != 0])


def create_a_ball(screen):
    color = random.choice(BALL_COLORS)
    position_x = random.randint(Config.BALL_RADIUS, screen.get_width() - Config.BALL_RADIUS)
    position_y = random.randint(Config.TOP_BAR_HEIGHT + Config.BALL_RADIUS,
                                screen.get_height() - Config.BALL_RADIUS)
    position = [position_x, position_y]
    velocity = [get_non_zero_velocity(), get_non_zero_velocity()]
    ball = Ball(screen, color, position, velocity)
    return ball


def create_balls(screen, number_of_balls):
    balls = []
    for _ in range(number_of_balls):
        ball = create_a_ball(screen)
        balls.append(ball)
    return balls


def merge_balls_if_collide(screen, balls):
    selected_ball = None
    for ball in balls:
        if ball.isSelected:
            selected_ball = ball
            break

    if selected_ball is None:
        return  # No ball is selected, so nothing to do

    i = 0
    while i < len(balls):
        if balls[i].isSelected:
            i += 1
            continue  # Skip the selected ball

        ball = balls[i]
        # Calculate distance between the selected ball and this ball
        distance_squared = (selected_ball.position[0] - ball.position[0]) ** 2 + (
                selected_ball.position[1] - ball.position[1]) ** 2
        if selected_ball.color == ball.color and distance_squared < (selected_ball.radius + ball.radius) ** 2:
            # Balls have the same color and collide, merge logic:
            # Increase the selected ball's radius. Here you might adjust the formula
            # depending on how you want the game's physics to behave (e.g., conserving volume)
            selected_ball.radius = (selected_ball.radius ** 3 + ball.radius ** 3) ** (1 / 3)

            # Remove the non-selected ball
            balls.pop(i)
            # Adjust the number of new balls as needed
            for k in range(1):
                new_ball = create_a_ball(screen)
                balls.append(new_ball)

            # No need to decrement i, as we want the next loop iteration to check the new current index
        else:
            i += 1  # Only increment if no merge occurs

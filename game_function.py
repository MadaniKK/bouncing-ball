import pygame
import random
from ball import Ball

BALL_COLORS = [
    (0, 255, 0),  # Green
    (255, 255, 0),  # Yellow
    (0, 0, 255),  # Blue
    (255, 20, 147)  # Pink, using the DeepPink RGB value as an example
]


def get_non_zero_velocity(min_val=-3, max_val=3):
    return random.choice([i for i in range(min_val, max_val + 1) if i != 0])


def create_balls(screen, number_of_balls):
    balls = []
    for _ in range(number_of_balls):
        color = random.choice(BALL_COLORS)
        position = [random.randint(20, 780), random.randint(20, 580)]
        velocity = [get_non_zero_velocity(), get_non_zero_velocity()]
        ball = Ball(screen, color, position, velocity)
        balls.append(ball)
    return balls

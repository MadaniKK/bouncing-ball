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


def create_balls(screen, game_state):
    balls = []
    balls_dict = {}
    for _ in range(game_state.ball_count):
        color = random.choice(BALL_COLORS)
        position_x = random.randint(Config.BALL_RADIUS, screen.get_width() - Config.BALL_RADIUS)
        position_y = random.randint(Config.TOP_BAR_HEIGHT + Config.BALL_RADIUS, screen.get_height() - Config.BALL_RADIUS)
        position = [position_x, position_y]
        velocity = [get_non_zero_velocity(), get_non_zero_velocity()]
        ball = Ball(screen, color, position, velocity)
        balls.append(ball)
        balls_dict[ball.id] = ball
    return balls

import pygame
import random
from ball import Ball
from config import Config

BALL_COLORS = [
    (0, 255, 0),  # Green
    (255, 255, 0),  # Yellow
    (0, 0, 255),  # Blue
    (255, 20, 147),  # Pink (DeepPink)
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (0, 255, 255),  # Cyan
    (255, 0, 0),  # Red
    (165, 42, 42),  # Brown
    (255, 192, 203),  # LightPink
    (128, 128, 128),  # Gray
    (0, 128, 0),  # DarkGreen
    (0, 0, 128),  # Navy
    (128, 0, 0),  # Maroon
    (75, 0, 130),  # Indigo
    (255, 69, 0),  # OrangeRed
    (0, 206, 209),  # DarkTurquoise
    (148, 0, 211),  # DarkViolet
]


def get_non_zero_velocity(min_val=-3, max_val=3):
    return random.choice([i for i in range(min_val, max_val + 1) if i != 0])


def create_balls(screen, game_state):
    balls = []
    balls_dict = {}
    available_colors = BALL_COLORS[: game_state.color_count]
    for _ in range(game_state.ball_count):
        color = random.choice(BALL_COLORS)
        position_x = random.randint(
            Config.BALL_RADIUS, screen.get_width() - Config.BALL_RADIUS
        )
        position_y = random.randint(
            Config.TOP_BAR_HEIGHT + Config.BALL_RADIUS,
            screen.get_height() - Config.BALL_RADIUS,
        )
        position = [position_x, position_y]
        velocity = [get_non_zero_velocity(), get_non_zero_velocity()]
        ball = Ball(screen, color, position, velocity)
        balls.append(ball)
        balls_dict[ball.id] = ball
    return balls

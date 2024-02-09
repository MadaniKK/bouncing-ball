import pygame
import random
import uuid
from config import Config


class Ball:
    def __init__(self, screen, color, position, velocity, radius=10):
        """
            Initializes a new Ball instance.

            Args:
                screen (pygame.Surface): The pygame screen surface where the ball will be drawn.
                color (tuple): The color of the ball, an (R, G, B) tuple where each component is an integer
                                ranging from 0 to 255.
                position (list): The initial position of the ball on the screen, a list of two integers: [x, y].
                velocity (list): The initial velocity of the ball, a list of two integers: [vx, vy].
                                Positive values move the ball right/down, and negative values move it left/up.
                radius (int): The radius of the ball, set to 10 pixels by default.
            Attributes:
                isSelected (bool): If the ball is selected by the mouse
        """
        self.id = uuid.uuid4()
        self.screen = screen
        self.color = color
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.isSelected = False
        self.isDragging = False

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] <= 0 + self.radius or self.position[
            0] >= self.screen.get_width() - self.radius:
            self.velocity[0] *= -1
        if self.position[1] <= Config.TOP_BAR_HEIGHT + self.radius or self.position[1] >= self.screen.get_height() - self.radius:
            self.velocity[1] *= -1

    def attract_others(self, balls):
        if not self.isSelected:
            return  # Skip if this ball is not selected
        for ball in balls:
            if ball.color == self.color and ball != self:
                # Move ball towards the selected ball
                if ball.position[0] < self.position[0]:
                    ball.velocity[0] = abs(ball.velocity[0])
                else:
                    ball.velocity[0] = -abs(ball.velocity[0])
                if ball.position[1] < self.position[1]:
                    ball.velocity[1] = abs(ball.velocity[1])
                else:
                    ball.velocity[1] = -abs(ball.velocity[1])

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

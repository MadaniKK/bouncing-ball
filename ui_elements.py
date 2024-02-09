import pygame


class UIManager:
    pygame.font.init()  # Initialize the font module
    default_font = pygame.font.Font(None, 24)  # Define a default font as a class attribute

    @staticmethod
    def draw_top_bar(screen, text, font=default_font, bar_height=30, color=(200, 200, 200), text_color=(0, 0, 0)):
        """
        Draws a top bar with text on a given Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame screen to draw on.
            font (pygame.font.Font): The font to use for the text.
            text (str): The text to display on the top bar.
            bar_height (int): The height of the top bar.
            color (tuple): The color of the top bar (RGB).
            text_color (tuple): The color of the text (RGB).
        """
        pygame.draw.rect(screen, color, pygame.Rect(0, 0, screen.get_width(), bar_height))
        text_surface = font.render(text, True, text_color)
        screen.blit(text_surface, (10, 5))



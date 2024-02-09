from config import Config


class GameState:
    def __init__(self):
        self.ball_count = Config.DEFAULT_BALL_COUNT
        self.color_count = Config.DEFAULT_COLOR_COUNT
        # Other dynamic states like current score, levels, etc.
        self.current_clicked_balls_count = 0

    def update_ball_count(self, new_count):
        self.ball_count = new_count

    # Add more methods to update and manage game state as needed

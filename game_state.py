from config import Config
from system_metrics import collect_metrics


class GameState:
    def __init__(self):
        self.system_metrics = {
            "cpu_utilization": 17.9,
            "memory_usage": 79.0,
            "process_count": 421,
        }  # Example metrics
        self.ball_count = self.calculate_ball_count()
        self.color_count = self.calculate_color_count()
        # Other dynamic states like current score, levels, etc.
        self.current_clicked_balls_count = 0

    def calculate_ball_count(self):
        # Increase ball count based on CPU utilization
        cpu_utilization = self.system_metrics["cpu_utilization"]
        additional_balls = int(
            cpu_utilization / 10
        )  # Simplified logic for demonstration
        return Config.DEFAULT_BALL_COUNT + additional_balls

    def calculate_color_count(self):
        # Adjust color count based on the number of processes
        process_count = self.system_metrics["process_count"]
        additional_colors = int(
            process_count / 50
        )  # Simplified logic for demonstration
        return max(
            Config.DEFAULT_COLOR_COUNT, additional_colors
        )  # Ensure at least the default count

    def update_system_metrics(self, new_metrics):
        self.system_metrics = new_metrics
        # Recalculate ball and color counts when metrics are updated
        self.ball_count = self.calculate_ball_count()
        self.color_count = self.calculate_color_count()

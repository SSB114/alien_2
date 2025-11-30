class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # 尝试从文件加载最高分
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """从文件加载最高分，如果文件不存在则返回0"""
        try:
            with open('high_score.txt', 'r') as f:
                return int(f.read())
        except (FileNotFoundError, ValueError):
            return 0
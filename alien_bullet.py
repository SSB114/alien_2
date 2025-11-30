import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """管理外星人发射的子弹"""
    
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color
        
        # 创建子弹矩形并设置位置（从外星人底部发出）
        self.rect = pygame.Rect(
            0, 0, 
            self.settings.alien_bullet_width, 
            self.settings.alien_bullet_height
        )
        self.rect.midbottom = alien.rect.midbottom
        
        # 存储精确位置
        self.y = float(self.rect.y)
    
    def update(self):
        """向下移动子弹"""
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
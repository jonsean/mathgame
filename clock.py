# clock.py
import pygame
import time

class Clock:
    def __init__(self, font_size=48, color=(255, 255, 255), position=(10, 10), font_name=None):
        self.start_time = time.time()
        self.paused_time = 0
        self.is_paused = False
        self.pause_start = 0
        
        self.font_size = font_size
        self.color = color
        self.position = position
        self.font = pygame.font.SysFont(font_name, font_size)
        
        # Background for better visibility
        self.background_color = (0, 0, 0)
        self.background_offset = 5
        
    def reset(self):
        """Reset the clock to 00:00"""
        self.start_time = time.time()
        self.paused_time = 0
        self.is_paused = False
        self.pause_start = 0
    
    def pause(self):
        """Pause the clock"""
        if not self.is_paused:
            self.is_paused = True
            self.pause_start = time.time()
    
    def unpause(self):
        """Unpause the clock"""
        if self.is_paused:
            self.paused_time += time.time() - self.pause_start
            self.is_paused = False
            self.pause_start = 0
    
    def get_elapsed_time(self):
        """Get elapsed time in seconds"""
        current_time = time.time()
        if self.is_paused:
            return self.pause_start - self.start_time - self.paused_time
        else:
            return current_time - self.start_time - self.paused_time
    
    def get_time_string(self):
        """Get formatted time string MM:SS"""
        elapsed = self.get_elapsed_time()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def draw(self, surface):
        """Draw the clock on the surface"""
        time_text = self.get_time_string()
        
        # Render background text (for outline effect)
        background_rendered = self.font.render(time_text, True, self.background_color)
        # Render main text
        text_rendered = self.font.render(time_text, True, self.color)
        
        # Draw background text slightly offset
        surface.blit(background_rendered, (self.position[0] + self.background_offset, 
                                         self.position[1] + self.background_offset))
        # Draw main text
        surface.blit(text_rendered, self.position)
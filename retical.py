import pygame

class Retical:
    def __init__(self, cursor_path = 'retical.png', alt_cursor_path = 'stopRetical.png'):
        self.cursor_path = cursor_path
        self.alt_cursor_path = alt_cursor_path
        self.set_cursor_path()
        pygame.mouse.set_visible(False)
        
    def set_cursor_path(self):
        self.cursor_img = pygame.image.load(self.cursor_path).convert_alpha()
        self.cursor_size = self.cursor_img.get_size()
    
    def set_alt_path(self):
        self.cursor_img = pygame.image.load(self.alt_cursor_path).convert_alpha()
        self.cursor_size = self.cursor_img.get_size()
        

    def draw(self, surface):
        mx, my = pygame.mouse.get_pos()
        x = mx - self.cursor_size[0] // 2
        y = my - self.cursor_size[1] // 2
        surface.blit(self.cursor_img, (x, y))
    
    
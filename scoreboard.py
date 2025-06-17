import pygame

class ScoreBoard:
    def __init__(self, score = 0, pos = (0,0), font_size=200, color=(255, 100, 255), font_name=None):
        self.score = score
        self.text = "Score: " + str(score) 
        self.pos = pos
        self.font_size = font_size
        
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.rendered = self.font.render(self.text, True, color)
        
        self.offset = 4
        self.background_pos = self.get_background_pos()
        self.backgroundColor = (0,0,0)
        self.backgroundFont = pygame.font.SysFont(font_name, font_size)
        self.backgroundRendered = self.backgroundFont.render(self.text, True, self.backgroundColor)
        
    def get_background_pos(self):
        return (self.pos[0] + self.offset, self.pos[1])
        
    def setScore(self, score):
        self.score = score
        self.set_text("Score: " + str(score)) 

         
    def draw(self, surface):
        surface.blit(self.backgroundRendered, self.background_pos)
        surface.blit(self.rendered, self.pos)

    def set_text(self, new_text):
        self.text = new_text
        self.rendered = self.font.render(new_text, True, self.color)
        self.backgroundRendered = self.backgroundFont.render(new_text, True, self.backgroundColor)
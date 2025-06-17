import pygame
import random

class MathProblem:
    def __init__(self, maxnum = 10, end_pos = (500,600), start_pos=(500,100), font_size=200, color=(255, 100, 255), font_name=None):
        self.maxnum = maxnum
        self.text = "" 
        self.ans = 0
        self.end_pos = end_pos
        self.current_pos = start_pos
        self.start_pos = start_pos
        self.font_size = font_size
        
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.rendered = self.font.render(self.text, True, color)
        
        self.offset = 4
        self.background_pos = self.get_background_pos()
        self.backgroundColor = (0,0,0)
        self.backgroundFont = pygame.font.SysFont(font_name, font_size)
        self.backgroundRendered = self.backgroundFont.render(self.text, True, self.backgroundColor)
        
        self.setProblem()
    def get_background_pos(self):
        return (self.current_pos[0] + self.offset, self.current_pos[1])
    def setProblem(self, end_pos = (500,600), start_pos=(500,100), font_size=200):
        self.end_pos = end_pos
        self.start_pos = start_pos
        self.font_size = font_size
        cmin = 0
        cmax = 255
        r = random.randint(cmin,cmax)
        g = random.randint(cmin,cmax)
        b = random.randint(cmin,cmax)
        self.color = (r,g,b)
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        self.ans = num1 + num2
        self.set_text(str(num1) + "+" + str(num2) + "=") 
        self.current_pos = self.start_pos
        
    def animate(self):
        difx = self.end_pos[0] - self.start_pos[0]
        dify = self.end_pos[1] - self.start_pos[1]
        steps = 100
        deltax = difx/steps
        deltay = dify/steps
        if difx > 0: 
            if self.current_pos[0] < self.end_pos[0]:
                self.current_pos = (self.current_pos[0]+deltax, self.current_pos[1])
        else: 
            if self.current_pos[0] > self.end_pos[0]:
                self.current_pos = (self.current_pos[0]+deltax, self.current_pos[1])
        if dify > 0:
            if self.current_pos[1] < self.end_pos[1]:
                self.current_pos = (self.current_pos[0], self.current_pos[1]+deltay)
        else: 
            if self.current_pos[1] > self.end_pos[1]:
                self.current_pos = (self.current_pos[0], self.current_pos[1]+deltay)
                
        self.background_pos = self.get_background_pos()
         
    def draw(self, surface):
        surface.blit(self.backgroundRendered, self.background_pos)
        surface.blit(self.rendered, self.current_pos)

    def set_text(self, new_text):
        self.text = new_text
        self.rendered = self.font.render(new_text, True, self.color)
        self.backgroundRendered = self.backgroundFont.render(new_text, True, self.backgroundColor)

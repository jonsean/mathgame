import pygame
from pygame.locals import *
from astroid import Astroid
from mathProblem import MathProblem
from retical import Retical
from scoreboard import ScoreBoard
import numpy as np
import random
pygame.init()
class App:
    charlist = ""
    def __init__(self):
        
        self._running = True
        self.mainScreen = None
        #self.info = pygame.display.Info()
        self.size = self.width, self.height = 1334, 750
        
        
        
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        
        # timers 
        self.AstroidSpawn_Event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.AstroidSpawn_Event, 250)
        
        self.IncorrectTimeout_Event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.IncorrectTimeout_Event, 2000)
        
        # init screen
        self.mainScreen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        #self.mainScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
        # set cursor 
        self.cursor = Retical()
        
        # set math problem
        self.p_size = 200
        self.mathLabel = MathProblem(end_pos = (self.width/2 - self.p_size,self.height - self.p_size), 
                                    start_pos=(self.width/2 - self.p_size,0), font_size=self.p_size)
        self.answersOut = 0
        
        self.scoreboard = ScoreBoard()
        
        self.astroidList = []
        
        self.score = 0
        
        # audio
        self.play_audio = True
        self.sound_array = [] # to easilly change all sounds
        self.sound_correct = pygame.mixer.Sound('correct.mp3')
        self.sound_array.append(self.sound_correct)
        self.sound_incorrect = pygame.mixer.Sound('incorrect.mp3') 
        self.sound_array.append(self.sound_incorrect)
        self.sound_music = pygame.mixer.Sound('music1.mp3')
        self.sound_array.append(self.sound_music)
        self.sound_music.play(loops = -1)
        
        self.canClick = True
        
        self._running = True
        
    def correctAnswer(self):
        self.score += 1
        self.scoreboard.setScore(self.score)
        if self.play_audio:
            self.sound_correct.play()
        
        print("Correct!")
        print("Score:" + str(self.score))
        self.mathLabel.setProblem(end_pos = (self.width/2 - self.p_size,self.height - self.p_size), 
                                    start_pos=(self.width/2 - self.p_size,0), font_size=self.p_size)
        self.answersOut = 0
    
    def incorrectAnswer(self):
        self.cursor.set_alt_path()
        self.canClick = False 
        self.score -= 1
        self.scoreboard.setScore(self.score)
        if self.play_audio:
            self.sound_incorrect.play()
        
        print("Oh NO!")
        print("Score:" + str(self.score))
    
    def astroidClicked(self, astroid):
        if astroid.label_text == str(self.mathLabel.ans):
            self.correctAnswer()
        else: 
            self.incorrectAnswer()
        self.remove_astroid(astroid)
    
    def add_astroid(self):
        ans = self.mathLabel.ans
        if self.answersOut < 2 and random.random() > .2:
            num = random.randint(ans-1, ans+1)
            if num == ans:
                self.answersOut += 1
        else: 
            num = random.randint(0,20)
        
        x = random.randint(0, self.width)
        y = 0
        radius = 30 + num
        a = Astroid(radius, position=(x, y), label_text = str(num))
        self.astroidList.append(a)
        
    def remove_astroid(self, astroid):
        if astroid.label_text == str(self.mathLabel.ans):
            self.answersOut -= 1
        self.astroidList.remove(astroid)
        
    def move_astroids(self):
        for i in self.astroidList:
            i.position = (i.position[0] + i.velocity[0], i.position[1] + i.velocity[1])
            if i.position[1] > self.height:
                self.remove_astroid(i)
    
    def set_screen_size(self):
        self.size = self.width, self.height = self.mainScreen.get_size()
       
    def change_volume(self, delta=.1):
        for i in self.sound_array:
            try: 
                i.set_volume(i.get_volume() + delta)
            finally:
                print("volume:" + str(i.get_volume()))
    
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.canClick:
            #check if astroid is clicked
            for i in self.astroidList:
                if i.containts(event.pos):
                    self.astroidClicked(i)
        if event.type == self.AstroidSpawn_Event:
            self.add_astroid()
        if event.type == pygame.KEYDOWN:
            nlist = self.charlist + event.unicode
            self.charlist = nlist
            print(event, nlist)
            if event.key == 1073741905:
                self.change_volume(-.1)
            if event.key == 1073741906:
                self.change_volume(.1)
            if event.unicode == 's':
                if self.play_audio:
                    pygame.mixer.pause()
                    self.play_audio = False
                else: 
                    pygame.mixer.unpause()
                    self.play_audio = True
            if event.unicode == "\x1b":
                self._running = False
        if event.type == self.IncorrectTimeout_Event:
            self.canClick = True
            self.cursor.set_cursor_path()
        if event.type == pygame.WINDOWSIZECHANGED:
            self.set_screen_size()
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        self.dt = self.clock.tick(60)
        self.move_astroids()
        self.mathLabel.animate()
    def on_render(self):
        self.mainScreen.fill((0,0,200))
        #self.mainScreen.blit(self.img,(0,0))
        self.mathLabel.draw(self.mainScreen)
        self.scoreboard.draw(self.mainScreen)
        
        for i in self.astroidList:
            i.draw(self.mainScreen)
            
        self.cursor.draw(self.mainScreen)
        
        
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
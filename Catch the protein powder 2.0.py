# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:22:55 2024

@author: Caleben Jahn
"""

import pygame, simpleGE, random

class Protein(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Protein.jpg")
        self.setSize(25,25)
        self.reset()
        
    def reset(self):
        self.y=10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3,8)
    
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class scoreLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center =(50, 30)
        self.size = (80, 60)
        self.text = "Score"
        self.fgColor = "white"

class timeLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center =(550, 30)
        self.size = (80, 60)
        self.text = "Time"
        self.fgColor = "white"
    

class skinnyGuy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("skinnyGuy.png")
        self.setSize(50,50)
        self.position = (350, 450)
        self.moveSpeed = 5 
        
    def process(self): 
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Gym.jpg")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime=15
        self.score =0
        
        self.sndProtein = simpleGE.Sound("use.wav")
        
        
        self.skinnyGuy = skinnyGuy(self)
        self.Proteins = []
        for i in range(10):
            self.Proteins.append(Protein(self))
        self.scoreLabel = scoreLabel()
        self.timeLabel = timeLabel()
            
        self.sprites = [self.skinnyGuy, self.Proteins, self.scoreLabel, self.timeLabel]
        
        
    def process(self):
        for Protein in self.Proteins:
            if self.skinnyGuy.collidesWith(Protein):
               self.sndProtein.play()
               self.Protein.reset()
               self.score += 1
               self.scoreLabel.txt =f"Score:{self.score}"
        self.timeLabel.txt = f"{self.timer.getTimeleft()}"
        if self.timer.getTimeLeft() < 0:
            print (f"{self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
    #     print("I got to Instructions init")
        self.setImage("Gym.jpg")
        
        self.choice = "Play"
        self.instructions =simpleGE.MultiLabel()
        self.instructions.textLines = [
             "You're a very skinny guy, down on his luck with getting gains.",
             "An angel descendes and commands you to begin the grind",
             "You are placed into a gym, as protein powder falls from the sky",
             "Get as much protein as you can before the gym closes"]
        self.instructions.size = (550, 250)
        self.instructions.center = (320, 240)
        
        self.quitbutton=simpleGE.Button()
        self.quitbutton.text = "Quit"
        self.quitbutton.center= (500,350)
        
        self.playbutton = simpleGE.Button()
        self.playbutton.text = "Play"
        self.playbutton.center= (200, 350)
        
        self.prevScore = score
        self.scoreLabel = simpleGE.Label()
        self.scoreLabel = f"Previous score: {self.prevScore}"
        self.scoreLabel.center = (320, 400)
        
        self.sprites = [self.instructions, self.quitbutton, self.playbutton, self.scoreLabel]
        
    def process(self):
        if self.quitbutton.clicked:
            self.choice = "Quit"
            self.stop()
        if self.playbutton.clicked:
            self.choice = "Game"
            self.stop()
            
        if self.isKeyPressed(pygame.K_LEFT):
            self.choice= "Quit"
            self.stop()
        if self.isKeyPressed(pygame.K_RIGHT):
            self.choice= "Game"
            
               
               
            
def main():
    
    keepgoing = True
    score = 0
    while(keepgoing):
        instructions = Instructions(score)
        instructions.start()
        if instructions.choice == "Play":
            game = Game()
            game.start()
            score = game.score
        else:
            keepgoing = True

if __name__ == "__main__":
    main()
        
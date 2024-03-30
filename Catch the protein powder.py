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
    

class skinnyGuy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("skinnyGuy.png")
        self.setSize(60,60)
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
        
        self.sndProtein = simpleGE.Sound("use.wav")
        
        self.skinnyGuy = skinnyGuy(self)
        self.Protein = Protein(self)
        
        self.skinnyGuy = skinnyGuy(self)
        self.Proteins = []
        for i in range(10):
            self.Proteins.append(Protein(self))
            
        
        self.sprites = [self.skinnyGuy, self.Proteins]
        
    def process(self):
        for Protein in self.Proteins:
            if self.skinnyGuy.collidesWith(Protein):
               self.sndProtein.play()
               self.Protein.reset()
            
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
        
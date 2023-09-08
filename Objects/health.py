import pygame
import os 
import sys

def load_image(file_name):
    path = os.path.join(get_resource_path(), file_name)
    return pygame.image.load(path)

def get_resource_path():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    else:
        return ''
#Loads heart images
heart_l = load_image("resources/Sprites/Hearts/Heart 1.png")
heart_2 = load_image("resources/Sprites/Hearts/Heart 2.png")
heart_3 = load_image("resources/Sprites/Hearts/Heart 3.png")
heart_4 = load_image("resources/Sprites/Hearts/Heart 4.png")
dead_heart = load_image("resources/Sprites/Hearts/Dead Heart.png")

class Health:
    def __init__(self, screen):
        self.hp = 4
        self.frame_count = 0

    #Draws corresponding hearts based on health
    def draw(self, screen):
        if self.hp == 4:
            screen.blit(heart_4, (155, 20))
            screen.blit(heart_3, (110, 20))
            screen.blit(heart_2, (65, 20))
            screen.blit(heart_l , (20, 20))
        if self.hp == 3:
            screen.blit(dead_heart, (155, 20))
            screen.blit(heart_3, (110, 20))
            screen.blit(heart_2, (65, 20))
            screen.blit(heart_l, (20, 20))
        if self.hp == 2:
            screen.blit(dead_heart, (155, 20))
            screen.blit(dead_heart, (110, 20))
            screen.blit(heart_2, (65, 20))
            screen.blit(heart_l, (20, 20))
        if self.hp == 1:
            screen.blit(heart_l, (20, 20))
            screen.blit(dead_heart, (65, 20))
            screen.blit(dead_heart, (110, 20))
            screen.blit(dead_heart, (155, 20))
        if self.hp <= 0:
            #game_over()
            screen.blit(dead_heart, (20, 20))
            screen.blit(dead_heart, (65, 20))
            screen.blit(dead_heart, (110, 20))
            screen.blit(dead_heart, (155, 20))
            return

    #Tracks damage taken
    def damage(self, damaged):
        if not damaged:
            self.hp -= 1
    
    def game_over(self):
        return self.hp <= 0

        

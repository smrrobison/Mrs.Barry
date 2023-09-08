import os
import sys
import pygame
class Counter:
    def __init__(self):
        self.value = 0
        self.high_score = self.get_high_score()
        self.font_size = 36
        self.font = pygame.font.Font(None, self.font_size)
        self.color = (255, 255, 255)
        

    def increment(self, dt):
        self.value += 1

    def draw(self, screen, x, y):
        text = self.font.render(f"Score: {self.value}", True, self.color)
        screen.blit(text, (x, y))

    def get_high_score(self):
        try:
            with open("resources/Text Files/high_score.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            # If the file is not found (first-time run or no high score saved yet), return 0
            high_score = 0

        return high_score

    def save_high_score(self):
        if self.value > self.high_score:
            self.high_score = self.value
            with open("resources/Text Files/high_score.txt", "w") as file:
                file.write(str(self.value))

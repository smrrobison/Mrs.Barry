import pygame
import os
import sys
from Objects.startwindow import start_screen
from Objects.game import Game

def load_sound(file_name):
    path = os.path.join('resources', 'Sound Files', file_name)
    return pygame.mixer.Sound(path)

#Initiates main game
pygame.init()
window_width, window_height = 1280, 720
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mrs. Barry")
clock = pygame.time.Clock()
game = Game(screen, clock)
running = True
exit_game = False
main_menu = True
music = False

pygame.mixer.init()

sound = load_sound("music.mp3")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if main_menu:
        sound.stop()
        play, exit_game = start_screen(screen, window_width, window_height, game.counter.high_score)
        main_menu = False
        music = True
        #Resets the game
        game = Game(screen, clock)
        
    if play: 
        play, main_menu = game.play()
        pygame.display.flip()
        if music:
            sound.set_volume(.2)  # Adjust the volume as needed
            sound.play(-1)
            music = False

    if exit_game:
        pygame.quit()

pygame.quit()
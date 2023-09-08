import pygame
import os
import sys

from Objects.player import Player
from Objects.enemy import Enemy
from Objects.health import Health
from Objects.counter import Counter

def load_image(file_name):
    path = os.path.join(get_resource_path(), file_name)
    return pygame.image.load(path)

def get_resource_path():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    else:
        return ''

background_image = load_image("resources/Sprites/office.png")

class Game:
    def __init__(self, screen, clock):
        self.player = Player(screen)
        self.health = Health(screen)
        self.counter = Counter()
        self.enemies = []
        self.frame_count = 0
        self.keep_playing = True
        self.main_menu = False
        self.screen = screen
        self.clock = clock
        self.dt = 0
        self.prev_score = 0
        self.enemy_speed = 2
        self.spawn_rate = 200

    def play(self):
        #Refreshes screen
        self.screen.fill("white")
        self.screen.blit(background_image, (0, 0))
        self.health.draw(self.screen)
    
        #controls enemy spawn rate
        if self.frame_count % self.spawn_rate == 0:
            new_enemy = Enemy(self.player.x, self.player.y, 50, 50, (255, 0, 0), self.get_difficulty())
            self.enemies.append(new_enemy)

        #controls enemy behavior
        for enemy in self.enemies:
            enemy.move(self.player.x, self.player.y)
            enemy.draw(self.screen)
            #create boundaries to prevent enemy from moving into hit boxes if collisions are true
            if enemy.check_collision(self.player.get_hitbox()):
                self.health.damage(self.player.damaged)
                self.player.damage()
                #Checks for game over state 
            if self.health.game_over():
                self.main_menu = True
                self.keep_playing = False
                self.counter.save_high_score()
            if enemy.check_collision(self.player.hammer):
                #player gets a point
                enemy.die()
                self.counter.increment(self.screen)

        #Counter instantiation
        self.counter.draw(self.screen, 20, 65)  # Adjust the position of the counter on the screen

        #controls player behavior
        self.player.draw(self.screen, self.frame_count)    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.keep_playing = False
            self.main_menu = True
            self.counter.save_high_score()

        self.player.move(keys, self.dt, self.frame_count)

        #Tracks frames/frame rate
        self.dt = self.clock.tick(60) / 1000
        self.frame_count += 1
        return self.keep_playing, self.main_menu

    def get_difficulty(self):
        score = self.counter.value
        if (score - self.prev_score) >= 5:
            self.prev_score = score
            if self.enemy_speed < 5:
                self.enemy_speed += .10
            if self.spawn_rate > 20:
                self.spawn_rate -= 20
            return self.enemy_speed
        return self.enemy_speed

import pygame
import os
import sys
import math
import random

def load_image(file_name):
    path = os.path.join('resources','Sprites', file_name)
    return pygame.image.load(path)


def load_sound(file_name):
    path = os.path.join('resources', 'Sound Files', file_name)
    return pygame.mixer.Sound(path)


pygame.mixer.init()

splat1 = load_sound("splat1.mp3")
splat2 = load_sound("splat2.mp3")
splat3 = load_sound("splat3.mp3")
splat4 = load_sound("scream.mp3")

    
class Enemy:
    def __init__(self, player_x, player_y, width, height, color, difficulty):
        self.x, self.y = self.get_random_spawn_point(player_x, player_y)
        self.image = self.get_image()
        self.width = width
        self.height = height
        self.color = color
        self.dead = False
        self.speed = difficulty
        self.touching = False

    def move(self, player_x, player_y):
        if (not self.dead) and (not self.touching):
            # Calculate direction vector from enemy to player
            dx = player_x - self.x
            dy = player_y - self.y

            # Normalize the direction vector
            length = math.sqrt(dx**2 + dy**2)
            
            if length != 0:
                dx /= length
                dy /= length

            # Update enemy position
            self.x += dx * self.speed
            self.y += dy * self.speed
            self.flip_image(player_x)
            self.check_boundary()

    def check_boundary(self):
        # Boundary checks to keep the bugs from going up top
        if self.y < 150: #top
            self.y = 150

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #Uncomment to draw enemy hitbox
        #pygame.draw.rect(screen, self.color, self.get_hitbox())
        

    def get_random_spawn_point(self, player_x, player_y):
        angle = random.uniform(0, 2 * math.pi)
        distance = 1000
        spawn_x = (1280 // 2) + distance * math.cos(angle)
        spawn_y = (720 // 2) + distance * math.sin(angle)

        if spawn_x <= player_x:
            self.right = False
        else:
            self.right = True

        #Ensures bugs don't spawn above 200 in height
        spawn_y = max(spawn_y, 200)
        
        #If spawn_y gets set to 200, this ensures the x-coordinate is off frame
        if (spawn_y == 200 and spawn_x < 1280 and spawn_x > 0):
            spawn_x = 1400
        
        return spawn_x, spawn_y

    def get_hitbox(self):
        if self.dead:
            return pygame.Rect(self.x, self.y, 0, 0)
        else: 
            return pygame.Rect(self.x, self.y, self.width - 5, self.height -5)

    def check_collision(self, hitbox):
        if pygame.Rect.colliderect(hitbox, self.get_hitbox()):
            self.touching = True
            return True
        else:
            self.touching = False
            return False

    def get_image(self):
        image = self.assign_image()

        if self.x <= 640:
            self.right = True
            return image
        else:
            self.right = False
            return pygame.transform.flip(image, True, False)
    
    def assign_image(self):
        self.img_num = random.randint(0, 3)

        if self.img_num == 0:
            return load_image("Bug 1.png")
        elif self.img_num == 1:
            return load_image("Bug 2.png")
        else:
            return load_image("Bug 3.png")
    
    def flip_image(self, player_x):

        if self.x <= player_x and not self.right:
            self.flip()
            self.right = True

        if self.x > player_x and self.right:
            self.flip()
            self.right = False
            
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def die(self):
        self.dead = True
        self.image = load_image("Splat.png")
        self.play_sound()

    def play_sound(self):
        sound = None
        random_number = random.randint(1, 3)

        if random_number == 1:
            sound = splat1
        elif random_number == 2:
            sound = splat2
        elif random_number == 3:
            random_number = random.randint(1, 3)
            if random_number == 1:
                sound = splat4   
            else:
                sound = splat3

        sound.set_volume(5)  
        sound.play(0)


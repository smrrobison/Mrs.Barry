import pygame
import random
import os 
import sys

# Get the directory of the script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_image(file_name):
    #path = os.path.join('resources', 'Sprites', file_name)
    return pygame.image.load(file_name)

def load_sound(file_name):
    #path = os.path.join('resources', 'Sound Files', file_name)
    return pygame.mixer.Sound(file_name)


image_l = load_image("Hammer Up.png")
image_r = pygame.transform.flip(image_l, True, False)
image_down_l = load_image("Hammer Down.png")
image_down_r = pygame.transform.flip(image_down_l, True, False)
image_red_l = load_image("Mrs Barry Hit.png")
image_red_r = pygame.transform.flip(image_red_l, True, False)

pygame.mixer.init()

hit1 = load_sound("hit1.mp3")
hit2 = load_sound("hit2.mp3")
hit3 = load_sound("hit3.mp3")
hit4 = load_sound("hit4.mp3")
hit5 = load_sound("hit4.mp3")

class Player:
    def __init__(self, screen):
        self.x, self.y = self.get_spawn_coordinates(screen)
        self.right = True
        self.damaged = False
        self.screen = screen 
        self.hammer_down = False
        self.frame_count = 0
        self.hammer = self.create_hammer()
        self.speed = 350
        self.hammer_frame = 0
        self.space_pressed = False
           
    def get_spawn_coordinates(self, screen):
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        return player_pos.x, player_pos.y

    def draw(self, screen, frame_count):
        #Uncomment to draw player hitbox
        #barry_color = (0,0, 255)
        #pygame.draw.rect(self.screen, barry_color, self.get_hitbox())
        
        if self.check_frames(self.frame_count, frame_count, 90):#change back to 90
            self.damaged = False
            self.frame_count = frame_count

        screen.blit(self.get_image(), (self.x, self.y))
        
    def get_hitbox(self):
        if self.right:
            return pygame.Rect(self.x - 2, self.y, self.get_image().get_width() / 2 + 27, self.get_image().get_height())
        else: 
            return pygame.Rect(self.x + 30, self.y, self.get_image().get_width() / 2 + 27, self.get_image().get_height())

    def move(self, keys, dt, frame_count):
        self.unhit(frame_count)
        if keys[pygame.K_w]:
            self.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.y += self.speed * dt
        if keys[pygame.K_a]:
            self.x -= self.speed * dt
            self.right = False
        if keys[pygame.K_d]:
            self.x += self.speed * dt
            self.right = True
        if keys[pygame.K_SPACE] and not self.space_pressed:
            self.hit(frame_count)
            self.space_pressed = True
        elif not keys[pygame.K_SPACE]:
            self.space_pressed = False
        self.check_boundary()

    def check_boundary(self):
        # Boundary checks to keep the player within the window
        if self.x < -10: #left
            self.x = -10
        if self.x > 1180: #right
            self.x = 1180
        if self.y < 120: #top
            self.y = 120
        if self.y > 640: #bottom
            self.y = 640

    def hit(self, frame_count):
        if (not self.damaged) and (self.check_frames(self.hammer_frame, frame_count, 5)):
            self.hammer_down = True
            self.hammer = self.create_hammer()
            self.hammer_frame = frame_count
    
    def unhit(self, frame_count):
        if self.check_frames(self.hammer_frame, frame_count, 5):
            self.hammer_down = False
            self.hammer = pygame.Rect(self.x, self.y, 0, 0)

    def create_hammer(self):
        if self.right:
            self.hammer = pygame.Rect(self.x + 80, self.y + 30, self.get_image().get_width() / 2 - 20, self.get_image().get_height() - 30)
        else:
            self.hammer = pygame.Rect(self.x - 5, self.y + 30, self.get_image().get_width() / 2 - 20, self.get_image().get_height() - 30)
        #Uncomment to draw hammer hitbox
        #hammer_color = (255, 0, 0)
        #pygame.draw.rect(self.screen, hammer_color, self.hammer)
        
        return self.hammer

    def damage(self):
        if self.damaged == False:
                self.play_sound()
                self.damaged = True
    
    def check_frames(self, last_frame, current_frame, modifier):
        if (abs(current_frame - last_frame)) >= modifier:
            return True
        else: 
            return False

    def get_image(self):
        if self.right:
            if self.damaged:
                return image_red_r
            else:
                if self.hammer_down:
                    return image_down_r
                else:
                    return image_r
        else: 
            if self.damaged:
                return image_red_l
            else:
                if self.hammer_down:
                    return image_down_l
                else:
                    return image_l

    def play_sound(self):
        sound = None
        random_number = random.randint(1, 5)
        
        if random_number == 1:
            sound = hit1
        elif random_number == 2:
            sound = hit2
        elif random_number == 3:
            sound = hit3
        elif random_number == 4:
            sound = hit4
        else:
            sound = hit5

        sound.set_volume(5)  
        sound.play(0)
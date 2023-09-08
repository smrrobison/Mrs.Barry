import pygame
import sys
import os

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):
        img = pygame.image.load(os.path.join(folder, filename)).convert()
        images.append(img)
    return images

def start_screen(screen, screen_width, screen_height, high_score):
    #start the start screen
    pygame.init()

    # Load image frames from the folder
    frames_folder = "resources/Video Files/Start Screen Frames"
    images = load_images_from_folder(frames_folder)

    # # Load the sound file for the background music
    pygame.mixer.init()
    bg_music = pygame.mixer.Sound("resources/Sound Files/Start Screen Aduio.mp3")
    bg_music.set_volume(5)  # Adjust the volume as needed

    # # Start playing the background music in a loop
    bg_music.play(-1)

    # Create a clock object to control frame rate for the start screen video
    clock = pygame.time.Clock()
    frame_rate = 15  # Adjust the frame rate as per your video's original frame rate
    frame_index = 0 # initial frame_index

    #set screen width, height, and caption
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mrs. Barry")
    
    #Title text & font instantiation "MRS BARRY"
    title_font = pygame.font.Font(None, 100)
    title_text = title_font.render("MRS BARRY", True, (255, 255, 255))
    title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2))
    
    #Subtitle text & font instantiation "Press SPACE to Start"
    subtitle_font = pygame.font.Font(None, 36)
    subtitle_text = subtitle_font.render("Press SPACE to Start", True, (255, 255, 255))
    subtitle_text_rect = subtitle_text.get_rect(center=(screen_width // 2, 430))

    #highscore title text & font instantiation "High Score: "
    highscore_font = pygame.font.Font(None, 36)
    highscore_text = highscore_font.render("High Score: ", True, (255, 255, 255))
    highscore_text_rect = subtitle_text.get_rect(center=(1200, 20))

    #Subtitle text & font instantiation <high_score>
    score_val_font = pygame.font.Font(None, 32)
    score_val_text = score_val_font.render(str(high_score), True, (255, 255, 255))
    score_val_text_rect = subtitle_text.get_rect(center=(1340, 22))
    
    # Timer variables for blinking text
    show_text = True
    blink_timer = 0
    blink_interval = 500  # Blink interval in milliseconds (e.g., 500ms = 0.5 seconds)
    
    #Core loop, exits when player presses SPACE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Stop the background music when the space bar is pressed
                bg_music.stop()
                return True, False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                return False, True

  
        #Display the current image frame
        screen.blit(images[frame_index], (0, 0))
        
        #Places text on top of the image
        screen.blit(title_text, title_text_rect)
        screen.blit(highscore_text, highscore_text_rect)
        screen.blit(score_val_text, score_val_text_rect)

        #Blink the subtitle text on and off based on the blink interval
        blink_timer += clock.get_time()
        if blink_timer >= blink_interval:
            show_text = not show_text
            blink_timer = 0

        if show_text:
            screen.blit(subtitle_text, subtitle_text_rect)
        
        pygame.display.flip()

        #Increment the frame index and loop back to the first frame if necessary
        frame_index = (frame_index + 1) % len(images)

        #Control the frame rate
        clock.tick(frame_rate)

if __name__ == "__main__":
    start_screen(1280, 720)
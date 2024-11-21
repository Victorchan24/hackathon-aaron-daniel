import pygame

pygame.mixer.init()

try:
    sound = pygame.mixer.Sound("sounds/C.wav")  # Replace with a known good file
    sound.play()
    pygame.time.wait(1000)  # Wait for 1 second to hear the sound
except Exception as e:
    print(f"Error loading sound: {e}")
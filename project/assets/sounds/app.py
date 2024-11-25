import pygame

# Initialize Pygame mixer
pygame.init()

# Load the sound files
catch_sound = pygame.mixer.Sound("assets/sounds/catch.wav")
miss_sound = pygame.mixer.Sound("assets/sounds/miss.wav")

# Play the sounds (for testing)
catch_sound.play()
pygame.time.delay(1000)  # Wait 1 second so the sound can play
miss_sound.play()
pygame.time.delay(1000)

pygame.quit()


if obj.colliderect(player):  # Caught the object
    catch_sound.play()
elif obj.top > HEIGHT:  # Missed the object
    miss_sound.play()
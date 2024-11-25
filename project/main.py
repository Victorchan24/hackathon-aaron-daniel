import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects!")

# Load sounds
catch_sound = pygame.mixer.Sound("catch.wav")
miss_sound = pygame.mixer.Sound("miss.wav")

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 100, 20
player = pygame.Rect(WIDTH // 2, HEIGHT - 40, player_width, player_height)
player_speed = 10

# Object settings
object_width, object_height = 30, 30
falling_objects = []
spawn_rate = 30  # Frames per new object
object_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Spawn falling objects
    if random.randint(1, spawn_rate) == 1:
        new_object = pygame.Rect(random.randint(0, WIDTH - object_width), 0, object_width, object_height)
        falling_objects.append(new_object)

    # Move falling objects
    for obj in falling_objects[:]:
        obj.y += object_speed
        if obj.colliderect(player):
            score += 1
            catch_sound.play()
            falling_objects.remove(obj)
        elif obj.top > HEIGHT:
            miss_sound.play()
            falling_objects.remove(obj)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw falling objects
    for obj in falling_objects:
        pygame.draw.rect(screen, RED, obj)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
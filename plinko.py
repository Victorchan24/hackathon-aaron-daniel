import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slither.io Clone")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
SNAKE_RADIUS = 10
SNAKE_SPEED = 5
snake_length = 5
snake_body = [(WIDTH // 2, HEIGHT // 2)]
direction = pygame.Vector2(1, 0)  # Initial direction: right

# Food settings
FOOD_RADIUS = 8
food_position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

# Score
score = 0

# Function to spawn food
def spawn_food():
    return (random.randint(FOOD_RADIUS, WIDTH - FOOD_RADIUS), 
            random.randint(FOOD_RADIUS, HEIGHT - FOOD_RADIUS))

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction.y == 0:  # Prevent reversing
                    direction = pygame.Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if direction.y == 0:
                    direction = pygame.Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                if direction.x == 0:
                    direction = pygame.Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if direction.x == 0:
                    direction = pygame.Vector2(1, 0)

    # Move snake
    head_x, head_y = snake_body[-1]
    new_head = (head_x + direction.x * SNAKE_SPEED, head_y + direction.y * SNAKE_SPEED)
    snake_body.append(new_head)

    # Keep snake within the screen bounds
    if new_head[0] < 0 or new_head[0] > WIDTH or new_head[1] < 0 or new_head[1] > HEIGHT:
        print("Game Over! You hit the wall.")
        running = False

    # Collision with self
    if new_head in snake_body[:-1]:
        print("Game Over! You hit yourself.")
        running = False

    # Check if snake eats the food
    dist = math.hypot(new_head[0] - food_position[0], new_head[1] - food_position[1])
    if dist < SNAKE_RADIUS + FOOD_RADIUS:
        food_position = spawn_food()
        score += 1
        snake_length += 1

    # Keep the snake at the right length
    if len(snake_body) > snake_length:
        snake_body.pop(0)

    # Draw food
    pygame.draw.circle(screen, RED, (int(food_position[0]), int(food_position[1])), FOOD_RADIUS)

    # Draw snake
    for segment in snake_body:
        pygame.draw.circle(screen, GREEN, (int(segment[0]), int(segment[1])), SNAKE_RADIUS)

    # Draw score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display and tick clock
    pygame.display.flip()
    clock.tick(30)  # Adjust to control speed

pygame.quit()
sys.exit()


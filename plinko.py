import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plinko Game")
clock = pygame.time.Clock()

# Constants
PEG_RADIUS = 5
BALL_RADIUS = 10
BIN_WIDTH = 80

# Peg positions
pegs = []
for row in range(5):  # 5 rows of pegs
    for col in range(10):  # 10 pegs per row
        x = (col + 0.5 * (row % 2)) * (WIDTH // 10)
        y = (row + 1) * 100
        pegs.append((x, y))

# Bins at the bottom
bins = [((i + 0.5) * BIN_WIDTH, HEIGHT - 20) for i in range(WIDTH // BIN_WIDTH)]

# Ball
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 2

    def move(self):
        self.vy += 0.1  # Simulate gravity
        self.x += self.vx
        self.y += self.vy

        # Bounce off pegs
        for peg_x, peg_y in pegs:
            if (self.x - peg_x) ** 2 + (self.y - peg_y) ** 2 < (PEG_RADIUS + BALL_RADIUS) ** 2:
                self.vx = random.uniform(-2, 2)
                self.vy = -abs(self.vy)

        # Stop at the bottom
        if self.y > HEIGHT - BALL_RADIUS:
            self.y = HEIGHT - BALL_RADIUS
            self.vy = 0
            self.vx = 0

# Create the first ball
balls = [Ball(WIDTH // 2, 50)]

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Drop a new ball from the mouse position
            x, y = pygame.mouse.get_pos()
            balls.append(Ball(x, y))

    # Draw pegs
    for peg_x, peg_y in pegs:
        pygame.draw.circle(screen, WHITE, (int(peg_x), int(peg_y)), PEG_RADIUS)

    # Draw bins
    for bin_x, bin_y in bins:
        pygame.draw.rect(screen, BLUE, (bin_x - BIN_WIDTH // 2, bin_y, BIN_WIDTH, 20))

    # Update and draw balls
    for ball in balls:
        ball.move()
        pygame.draw.circle(screen, YELLOW, (int(ball.x), int(ball.y)), BALL_RADIUS)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
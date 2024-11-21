import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 30)


# Game variables
score = 0
notes = ['a', 's', 'd', 'f', 'g', 'h', 'j']  # Keys for the game
note_timing = [1, 2, 3, 4]  # Timing of notes (in seconds)

# Create a note class
class Note:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)
    
    def move(self):
        self.y += 5  # Speed at which notes move down the screen
        self.rect.y = self.y

# Function to display text
def display_text(text, color, y_offset=0):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 + y_offset))

# Main game loop
def game_loop():
    global score
    running = True
    clock = pygame.time.Clock()
    notes_on_screen = []
    
    # Play the background music
    pygame.mixer.music.play()

    while running:
        screen.fill(BLACK)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    key = 'a'
                elif event.key == pygame.K_s:
                    key = 's'
                elif event.key == pygame.K_d:
                    key = 'd'
                elif event.key == pygame.K_f:
                    key = 'f'
                elif event.key == pygame.K_g:
                    key = 'g'
                elif event.key == pygame.K_h:
                    key = 'h'
                elif event.key == pygame.K_j:
                    key = 'j'
                else:
                    continue

                # Check if the player pressed the correct key at the right time
                note_to_check = [note for note in notes_on_screen if note.key == key and note.y > HEIGHT - 100]
                if note_to_check:
                    notes_on_screen.remove(note_to_check[0])
                    score += 1
                    display_text("Perfect!", GREEN, -50)
                else:
                    display_text("Missed!", RED, -50)

        # Add new notes to the screen
        if random.random() < 0.03:  # Control the frequency of notes
            note_key = random.choice(notes)
            note_y = 0  # Start at the top of the screen
            note_x = random.randint(100, WIDTH - 100)  # Random x position
            note = Note(note_key, note_x, note_y)
            notes_on_screen.append(note)
        
        # Move and draw notes
        for note in notes_on_screen:
            note.move()
            note.draw()

        # Display score
        display_text(f"Score: {score}", WHITE, 100)

        # Check for missed notes
        notes_on_screen = [note for note in notes_on_screen if note.y < HEIGHT]

        pygame.display.flip()
        clock.tick(60)

# Start the game
game_loop()
pygame.quit()

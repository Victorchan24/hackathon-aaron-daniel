import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
KEY_WIDTH = 70
KEY_HEIGHT = 200
OCTAVE = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
KEY_MAP = {
    pygame.K_a: 'C', pygame.K_s: 'D', pygame.K_d: 'E',
    pygame.K_f: 'F', pygame.K_g: 'G', pygame.K_h: 'A',
    pygame.K_j: 'B'
}

# Load sounds
SOUNDS = {note: pygame.mixer.Sound(f"sounds/{note}.wav") for note in OCTAVE}

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Virtual Piano")

# Draw piano keys
def draw_piano():
    for i in range(len(OCTAVE)):
        x = i * KEY_WIDTH
        pygame.draw.rect(screen, WHITE, (x, 0, KEY_WIDTH, KEY_HEIGHT))
        pygame.draw.rect(screen, BLACK, (x, 0, KEY_WIDTH, KEY_HEIGHT), 2)
        font = pygame.font.SysFont(None, 36)
        text = font.render(OCTAVE[i], True, BLACK)
        screen.blit(text, (x + KEY_WIDTH // 3, KEY_HEIGHT - 40))

# Play note
def play_note(note):
    if note in SOUNDS:
        SOUNDS[note].play()

# Main loop
def main():
    running = True
    while running:
        screen.fill(BLACK)
        draw_piano()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    play_note(KEY_MAP[event.key])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y <= KEY_HEIGHT:
                    index = x // KEY_WIDTH
                    if 0 <= index < len(OCTAVE):
                        play_note(OCTAVE[index])

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Run the program
if __name__ == "__main__":
    main()

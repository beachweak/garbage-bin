import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define screen dimensions and colors
WIDTH, HEIGHT = 1920, 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Musical Notes Changer")

# List of musical notes and chords
musical_elements = ["E7", "D5", "Gmaj7", "Cmaj", "Am", "Bm", "F#m", "Dmaj"]

def change_note():
    return random.choice(musical_elements)

current_note = change_note()
font = pygame.font.Font(None, 72)  # Larger font size

running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    text = font.render(current_note, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centered text
    screen.blit(text, text_rect)

    pygame.display.flip()

    if time.time() - start_time > 0.5:
        start_time = time.time()
        current_note = change_note()

# Quit pygame
pygame.quit()

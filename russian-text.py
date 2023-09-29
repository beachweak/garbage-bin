import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
BACKGROUND_COLOR = (0, 0, 0)  # Black background
TEXT_COLOR = (255, 255, 255)  # White text
TEXT_OPACITY = 128  # 50% opacity
FONT_SIZE = 48
DELAY_SECONDS = 2

# The phrase and words
phrase = "Псевдо растяжение звука во времени"
words = phrase.split()

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Animation")

# Load a font
font = pygame.font.Font(None, FONT_SIZE)

# Initialize variables
word_index = 0
word_timer = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Calculate text size and position
    word = words[word_index]
    text_surface = font.render(word, True, TEXT_COLOR)
    
    # Stretch text to fill the screen
    scaled_text_surface = pygame.transform.scale(text_surface, (WIDTH, HEIGHT))
    
    text_rect = scaled_text_surface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Adjust text opacity
    scaled_text_surface.set_alpha(TEXT_OPACITY)

    # Draw text
    screen.blit(scaled_text_surface, text_rect)
    pygame.display.flip()

    # Update word index and timer
    current_time = pygame.time.get_ticks()
    if current_time - word_timer >= DELAY_SECONDS * 1000:
        word_index = (word_index + 1) % len(words)
        word_timer = current_time

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()

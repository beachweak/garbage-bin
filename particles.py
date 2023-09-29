import pygame
import random

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Particle characteristics
PARTICLE_SIZE = 25  # Size of particles
PARTICLE_COLOR = (255, 255, 255)  # White
PARTICLE_LIFETIME = SCREEN_HEIGHT  # Distance particles will fall before renewing
PARTICLE_COUNT = 1000  # Number of particles

# Pygame initialization
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
PARTICLE_IMAGE = pygame.image.load("eelo.png")  # Load the particle image

# Class representing the particles
class Particle:
    def __init__(self):
        self.x = random.randrange(SCREEN_WIDTH)
        self.y = random.randrange(SCREEN_HEIGHT)
        self.speed = random.uniform(1, 4)

    def move(self):
        self.y += self.speed
        if self.y > PARTICLE_LIFETIME:
            self.y = 0
            self.x = random.randrange(SCREEN_WIDTH)

    def draw(self):
        SCREEN.blit(pygame.transform.scale(PARTICLE_IMAGE, (PARTICLE_SIZE, PARTICLE_SIZE)), (self.x, self.y))

# Create particles
particles = [Particle() for _ in range(PARTICLE_COUNT)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    SCREEN.fill((0, 0, 0))  # Fill the screen with black

    # Update and draw particles
    for particle in particles:
        particle.move()
        particle.draw()

    pygame.display.flip()
    CLOCK.tick(60)  # Set frame rate

# Quit Pygame
pygame.quit()
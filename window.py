import pygame
from astroid import Astroid
# --- Initialization ---
pygame.init()

# --- Screen Setup ---
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Polygon Example")

# --- Colors ---
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --- Polygon Vertex Points ---
# A triangle
triangle_points = [(350, 150), (250, 300), (450, 300)]

# A pentagon
pentagon_points = [
    (100, 100),
    (150, 50),
    (200, 100),
    (175, 150),
    (125, 150)
]

poly = Astroid()

# --- Main Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Drawing ---
    # Fill the background
    screen.fill(WHITE)

    # Draw a filled blue pentagon
    pygame.draw.polygon(screen, BLUE, pentagon_points)
    poly.draw(screen)
    # Draw a red triangle with a 5-pixel thick outline
    pygame.draw.polygon(screen, RED, triangle_points, 5)


    # --- Update the Display ---
    pygame.display.flip()

# --- Quit Pygame ---
pygame.quit()
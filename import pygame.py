import pygame

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0 )

# Dimension for gird screen

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20 
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60  

#Window of the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def main():
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

        pygame.quit()

        
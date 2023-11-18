import pygame
# Initializing Pygame
pygame.init()

# Defining color constants in RGB format
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0 )

# Defining dimensions for the grid screen
WIDTH, HEIGHT = 800, 800                      # Window width and height
TILE_SIZE = 20                                # Size of each tile/grid cell
GRID_WIDTH = WIDTH // TILE_SIZE               # Number of tiles across the width
GRID_HEIGHT = HEIGHT // TILE_SIZE             # Number of tiles across the height
FPS = 60                                      # Frames per second for the game


# Creating the window of the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting up a clock for FPS control
clock = pygame.time.Clock()


# Main function containing the game loop
def main():
    running = True
  
  
    # Game loop: runs as long as the game is running
    while running:
        # Limiting the loop to a maximum of FPS times per second
        clock.tick(FPS)
        
        # Event handling loop
        for event in pygame.event.get(): 
            # Checking for the QUIT event to exit the game
            if event.type == pygame.QUIT:
                running = False
        
        # Quitting Pygame when the game loop ends
        pygame.quit()

        
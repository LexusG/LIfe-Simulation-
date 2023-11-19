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

# Function to draw the grid on the screen
def draw_grid(positions):
    # Drawing horizontal lines for the grid
    for row in range (GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    
    # Drawing vertical lines for the grid
    for column in range (GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (column * TILE_SIZE, 0), (column * TILE_SIZE, HEIGHT))    


# Main function containing the game loop
def main():
    running = True
    
    positions = set()  # Set to store positions 
  
    # Game loop: runs as long as the game is running
    while running:
        # Limiting the loop to a maximum of FPS times per second
        clock.tick(FPS)
         
        # Event handling loop
        for event in pygame.event.get(): 
            # Checking for the QUIT event to exit the game
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(GREY)        # Filling the screen with grey background
        draw_grid(positions)     # Drawing the grid
        pygame.display.update()  # Updating the display after drawing
        
        # Quitting Pygame when the game loop ends
    pygame.quit()

if __name__=="__main__":
    main()       
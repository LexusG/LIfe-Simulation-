import pygame
# Initializing Pygame

import random

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

def gen(num):
    # Returning a set of tuples representing random positions on the grid
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])


# Function to draw the grid on the screen
def draw_grid(positions):
    # Drawing filled cells
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))


    # Drawing horizontal lines for the grid
    for row in range (GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    
    # Drawing vertical lines for the grid
    for column in range (GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (column * TILE_SIZE, 0), (column * TILE_SIZE, HEIGHT))  

# Function to adjust the grid based on the Game of Life rules
def adjust_grid(positions):
    # Sets to hold neighbor positions and new positions after adjustment
    all_neighbors = set()
    new_positions = set()
    
    # Iterating through each position to apply Game of Life rules
    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        # Filtering neighbors that are in current positions
        neighbors = list(filter(lambda x: x in positions, neighbors))

        # Applying the survival rule
        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    # Checking each neighbor position for possible birth of new cell
    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        # Applying the birth rule
        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions

# Function to get neighboring positions of a given cell
def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))

    return neighbors


# Main function containing the game loop
def main():
    running = True
    playing = False
    count = 0
    update_freq = 120  # Frequency of grid updates


    positions = set()  # Set to store positions 
  
    # Game loop: runs as long as the game is running
    while running:
        clock.tick(FPS) # Controlling the game's frame rate

        # Incrementing count if the game is in 'playing' mode
        if playing:
            count += 1

        # Updating the grid based on Game of Life rules at specific intervals
        if count >= update_freq:
            count = 0 
            positions = adjust_grid(positions)
        
        # Updating window title based on the game state
        pygame.display.set_caption("Playing" if playing else "Paused")

        # Event handling loop
        for event in pygame.event.get(): 
            # Checking for the QUIT event to exit the game
            if event.type == pygame.QUIT:
                running = False

             # Handling mouse button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # Getting mouse position
                col = x // TILE_SIZE           # Calculating column
                row = y // TILE_SIZE           # Calculating row
                pos= (col, row)                # Creating a tuple for the position

                # Creating a tuple for the position "FOR ADDING AND REMOVING POSITIONS" 
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
            
            # Handling keyboard inputs
            if event.type == pygame.KEYDOWN:
                # Toggling the play/pause state
                if event.key == pygame.K_SPACE:
                    playing = not playing  

                # For refreshing the game 
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0
                
                # Generating random positions
                if event.key == pygame.K_v:
                    positions = gen(random.randrange(2, 5)* GRID_WIDTH) 
                    

        screen.fill(GREY)        # Filling the screen with grey background
        draw_grid(positions)     # Drawing the grid
        pygame.display.update()  # Updating the display after drawing
        
        # Quitting Pygame when the game loop ends
    pygame.quit()

if __name__=="__main__":
    main()       
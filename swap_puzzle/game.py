import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# input text file to use for the game
grid = open("input/grid3.in", "r")

# extract dimensions of the grid from the first line of the input file
dimensions = grid.readline().split()
BOARD_WIDTH = int(dimensions[0])
BOARD_HEIGHT = int(dimensions[1])

# Size of a tile
TILE_SIZE = 200

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK=(0,0,0)

# Responsive game window
screen = pygame.display.set_mode((TILE_SIZE * BOARD_WIDTH, TILE_SIZE * BOARD_HEIGHT))
# Set up the game clock (frame rate)
clock = pygame.time.Clock()

# 2D array (game board representation)
board = []
for i in range(BOARD_HEIGHT):
    row = []
    for j in range(BOARD_WIDTH):
        row.append(i * BOARD_WIDTH + j)
    board.append(row)

# use the input file to set the board
for i in range(BOARD_HEIGHT):
    row = grid.readline().split()
    for j in range(BOARD_WIDTH):
        board[i][j] = int(row[j])
        

# initial selected tile (-1, -1 -> no tile is selected)
selected_row, selected_column = -1, -1

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Figure out which tile was clicked
            column = pos[0] // TILE_SIZE
            row = pos[1] // TILE_SIZE
            # If a tile is already selected, swap it with the clicked tile if they are adjacent
            if selected_row != -1 and selected_column != -1:
                # Check if the selected tile and the clicked tile are adjacent
                if (abs(selected_row - row) + abs(selected_column - column)) == 1:
                    # Swap the selected tile with the clicked tile
                    board[row][column], board[selected_row][selected_column] = board[selected_row][selected_column], board[row][column]
                    # Reset the selected tile
                    selected_row, selected_column = -1, -1
            # Otherwise, select the clicked tile
            else:
                selected_row, selected_column = row, column

    # Draw the game screen
    screen.fill(WHITE)
    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH):
            color = GRAY
            # Highlight the selected tile
            if row == selected_row and column == selected_column:
                color = (0, 255, 0)
            pygame.draw.rect(screen, color, (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)) # Draw tile
            pygame.draw.rect(screen, WHITE, (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)  # Draw border
            font = pygame.font.Font(None, 36) # Create a font object
            text = font.render(str(board[row][column]), True, WHITE) # Create a text surface
            text_rect = text.get_rect(center=(column * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))  # Center text
            screen.blit(text, text_rect) # Draw text

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

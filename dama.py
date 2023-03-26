import pygame

# Initialize Pygame
pygame.init()

# Set the size of the board and the size of each cell
board_size = (400, 400)
cell_size = (board_size[0]//8, board_size[1]//8)

# Create the board surface
board = pygame.Surface(board_size)

# Define colors for the cells and pieces
WHITE = (235, 236, 208)
BLACK = (119, 149, 86)
RED = (249, 249, 249)
BLUE = (87, 84, 82)

# Initialize the game board array
game_board = [[None for _ in range(8)] for _ in range(8)]

# Create game board with pieces
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 1:
            if row < 3:
                game_board[row][col] = 'R'
            elif row > 4:
                game_board[row][col] = 'B'

selected_piece = None

# Draw the board and pieces
def draw_board():
    for row in range(8):
        for col in range(8):
            cell_color = WHITE if (row + col) % 2 == 0 else BLACK
            cell_rect = pygame.Rect(col * cell_size[0], row * cell_size[1], cell_size[0], cell_size[1])
            pygame.draw.rect(board, cell_color, cell_rect)

            piece = game_board[row][col]
            if piece:
                piece_color = RED if piece == 'R' else BLUE
                piece_radius = cell_size[0] // 2 - 10
                piece_center = (col * cell_size[0] + cell_size[0] // 2, row * cell_size[1] + cell_size[1] // 2)
                pygame.draw.circle(board, piece_color, piece_center, piece_radius)

# Initialize the display window and blit the board onto it
window_size = (board_size[0] + 20, board_size[1] + 20)
window = pygame.display.set_mode(window_size)

# Run the game loop
running = True
while running:
    draw_board()
    window.blit(board, (10, 10))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = (y - 10) // cell_size[1], (x - 10) // cell_size[0]

            if game_board[row][col] is not None:
                selected_piece = (row, col)
            elif selected_piece is not None:
                game_board[row][col] = game_board[selected_piece[0]][selected_piece[1]]
                game_board[selected_piece[0]][selected_piece[1]] = None
                selected_piece = None

# Quit Pygame
pygame.quit()

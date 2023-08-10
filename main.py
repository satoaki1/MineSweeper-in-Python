import pygame
from constants import WIDTH, HEIGHT, TILE_SIZE
from board import Board

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


def main():
    board = Board(WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE, 40)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // TILE_SIZE
                row = y // TILE_SIZE

                if 0 <= col < board.width and 0 <= row < board.height:
                    if board.cells[col][row].adjacent_mines == 0:
                        board.reveal_empty(col, row)
                    else:
                        board.cells[col][row].is_revealed = True

                # Check game state after every click
                if board.is_game_over():
                    # Display game over screen (this could be a simple message using pygame's text rendering or a separate screen)
                    print("Game Over!")  # Replace with your desired action
                    run = False
                elif board.is_win():
                    # Display win screen
                    print("You Won!")
                    run = False

        for x in range(WIDTH // TILE_SIZE):
            for y in range(HEIGHT // TILE_SIZE):
                board.cells[x][y].draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

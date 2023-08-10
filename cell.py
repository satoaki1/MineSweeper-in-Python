from constants import *


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_flagged = False
        self.is_revealed = False
        self.adjacent_mines = 0

    def draw(self, win):

        # Draw base image
        img = GRID if not self.is_revealed else EMPTY
        win.blit(img, (self.x * TILE_SIZE, self.y * TILE_SIZE))

        if self.is_revealed:
            if self.is_mine:
                win.blit(MINE_CLICKED, (self.x * TILE_SIZE, self.y * TILE_SIZE))
            elif self.adjacent_mines:
                win.blit(NUMBERS[self.adjacent_mines], (self.x * TILE_SIZE, self.y * TILE_SIZE))
        elif self.is_flagged:
            win.blit(FLAG, (self.x * TILE_SIZE, self.y * TILE_SIZE))

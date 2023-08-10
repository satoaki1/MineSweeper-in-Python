import random
from cell import Cell


class Board:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.place_mines(mines)

    def place_mines(self, mines):
        for _ in range(mines):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

            # Make sure there is not already a mine here
            while self.cells[x][y].is_mine:
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.cells[x][y].is_mine = True

            # Update adjacent counts
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.cells[nx][ny].adjacent_mines += 1

    def reveal_empty(self, x, y):
        if not (0 <= x < self.width) or not (0 <= y < self.height):
            return
        cell = self.cells[x][y]
        if cell.is_revealed or cell.is_mine:
            return

        cell.is_revealed = True

        if cell.adjacent_mines == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    self.reveal_empty(x + dx, y + dy)

    def is_game_over(self):
        for row in self.cells:
            for cell in row:
                if cell.is_revealed and cell.is_mine:
                    return True
        return False

    def is_win(self):
        for row in self.cells:
            for cell in row:
                if cell.is_revealed and not cell.is_mine:
                    return False
        return True

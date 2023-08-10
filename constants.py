import pygame
import os

# Screen dimensions
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 32  # Change based on your tile size

# Load game assets
GRID = pygame.image.load(os.path.join("assets", "Grid.png"))
EMPTY = pygame.image.load(os.path.join("assets", "empty.png"))
FLAG = pygame.image.load(os.path.join("assets", "flag.png"))
MINE = pygame.image.load(os.path.join("assets", "mine.png"))
MINE_CLICKED = pygame.image.load(os.path.join("assets", "mineClicked.png"))
MINE_FALSE = pygame.image.load(os.path.join("assets", "mineFalse.png"))

NUMBERS = [
    None,  # No zero image
    pygame.image.load(os.path.join("assets", "grid1.png")),
    pygame.image.load(os.path.join("assets", "grid2.png")),
    pygame.image.load(os.path.join("assets", "grid3.png")),
    pygame.image.load(os.path.join("assets", "grid4.png")),
    pygame.image.load(os.path.join("assets", "grid5.png")),
    pygame.image.load(os.path.join("assets", "grid6.png")),
    pygame.image.load(os.path.join("assets", "grid7.png")),
    pygame.image.load(os.path.join("assets", "grid8.png")),
]


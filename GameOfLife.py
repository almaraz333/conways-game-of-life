import pygame
import numpy as np
import random

#colors of cells
col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (
    0,
    0,
    0,
)
col_grid = (30, 30, 60)


def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r - 1:r + 2, c - 1:c + 2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0
                                                          and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c * sz, r * sz, sz - 1, sz - 1))

    return nxt


def createRandomArray(
    size
):  #creates array of size n with 80% chance of each index to be 1 instead of 0
    arr = []
    for i in range(size):
        int = random.randint(0, 100)
        if int <= 80:
            arr.append(1)
        else:
            arr.append(0)
    return arr


def initGame(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([  #determines shape of starting pattern
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90),
        createRandomArray(90)
    ])
    pos = (30, 30)
    cells[pos[0]:pos[0] + pattern.shape[0],
          pos[1]:pos[1] + pattern.shape[1]] = pattern
    return cells


def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = initGame(dimx, dimy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(col_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()


if __name__ == "__main__":
    main(120, 90, 8)
import random

def create_grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        grid.append(row)
    return grid

def place_rooms(grid, num_rooms):
    rows = len(grid)
    cols = len(grid[0])

    for _ in range(num_rooms):
        while True:  # keep trying till empty spot
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)

            if grid[row][col] == 0:  # if spot is empty
                grid[row][col] = 1  # place room
                break  # exit loop and move to next room

grid = create_grid(5, 5)
num_rooms = random.randint(5, 10)

place_rooms(grid, num_rooms)
for row in grid:
    print(row)

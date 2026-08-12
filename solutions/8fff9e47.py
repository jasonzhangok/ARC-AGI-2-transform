def transform(grid):
    height = len(grid)
    width = len(grid[0])

    tiles = []
    for row in range(0, height, 2):
        for column in range(0, width, 2):
            tiles.append(
                (
                    grid[row][column],
                    grid[row][column + 1],
                    grid[row + 1][column],
                    grid[row + 1][column + 1],
                )
            )

    size = len(tiles)
    output = [[0 for _ in range(2 * size)] for _ in range(2 * size)]
    for row in range(2 * size):
        for column in range(2 * size):
            quadrant_row = row // size
            quadrant_column = column // size
            local_row = row % size
            local_column = column % size

            if quadrant_row == 0 and quadrant_column == 0:
                layer = min(local_row, local_column)
                corner = 0
            elif quadrant_row == 0:
                layer = min(local_row, size - 1 - local_column)
                corner = 1
            elif quadrant_column == 0:
                layer = min(size - 1 - local_row, local_column)
                corner = 2
            else:
                layer = min(size - 1 - local_row, size - 1 - local_column)
                corner = 3

            output[row][column] = tiles[size - 1 - layer][corner]

    return output

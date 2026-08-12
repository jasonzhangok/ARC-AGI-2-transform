def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    queue = []
    reached = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                queue.append((row, col))
                reached.add((row, col))

    for row, col in queue:
        for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (row + delta_row, col + delta_col)
            if (
                0 <= neighbor[0] < height
                and 0 <= neighbor[1] < width
                and grid[neighbor[0]][neighbor[1]] == 0
                and neighbor not in reached
            ):
                reached.add(neighbor)
                queue.append(neighbor)
                output[neighbor[0]][neighbor[1]] = 1

    return output

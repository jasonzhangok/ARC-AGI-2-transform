def transform(grid):
    height = len(grid)
    width = len(grid[0])
    border_top = 0
    border_left = 0
    border_size = 0
    for size in range(3, min(height, width) + 1):
        for top in range(height - size + 1):
            for left in range(width - size + 1):
                color = grid[top][left]
                if color == 0:
                    continue
                complete = True
                for offset in range(size):
                    if (grid[top][left + offset] != color
                            or grid[top + size - 1][left + offset] != color
                            or grid[top + offset][left] != color
                            or grid[top + offset][left + size - 1] != color):
                        complete = False
                if complete:
                    total_color = sum(value == color for row in grid for value in row)
                    if total_color == 4 * size - 4:
                        border_top = top
                        border_left = left
                        border_size = size
    output = []
    for row in range(border_top, border_top + border_size):
        output.append(grid[row][border_left:border_left + border_size])
    return output

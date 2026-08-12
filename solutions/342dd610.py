def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    displacements = {7: (-2, 0), 2: (0, -2), 9: (2, 0), 1: (0, 1)}
    points = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] in displacements:
                points.append((row, col, grid[row][col]))
                output[row][col] = 8
    for row, col, color in points:
        row_offset, col_offset = displacements[color]
        output[row + row_offset][col + col_offset] = color
    return output

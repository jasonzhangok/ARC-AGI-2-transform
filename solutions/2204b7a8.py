def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    full_rows = [(r, grid[r][0]) for r in range(height) if len(set(grid[r])) == 1 and grid[r][0] != 0]
    if len(full_rows) == 2:
        (first, color1), (second, color2) = full_rows
        midpoint = (first + second) / 2
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 3:
                    output[row][col] = color1 if row < midpoint else color2
    else:
        full_cols = [
            (c, grid[0][c])
            for c in range(width)
            if len({grid[r][c] for r in range(height)}) == 1 and grid[0][c] != 0
        ]
        (first, color1), (second, color2) = full_cols
        midpoint = (first + second) / 2
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 3:
                    output[row][col] = color1 if col < midpoint else color2
    return output



def transform(grid):
    h, w = len(grid), len(grid[0])
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    guides = [(c, value) for c, value in enumerate(grid[0]) if value != background]
    output = [row[:] for row in grid]
    for c, color in guides:
        for r in range(1, h):
            output[r][c] = background if grid[r][c] == color else color
    return output

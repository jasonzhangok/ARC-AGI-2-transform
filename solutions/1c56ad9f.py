

def transform(grid):
    height, width = len(grid), len(grid[0])
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    foreground = [(r, c) for r in range(height) for c in range(width) if grid[r][c] != background]
    bottom = max(r for r, _ in foreground)
    output = [[background] * width for _ in range(height)]
    for row, col in foreground:
        distance = bottom - row
        shift = -1 if distance % 4 == 1 else 1 if distance % 4 == 3 else 0
        output[row][col + shift] = grid[row][col]
    return output

from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    guides = [(c, value) for c, value in enumerate(grid[0]) if value != background]
    output = [row[:] for row in grid]
    for c, color in guides:
        for r in range(1, h):
            output[r][c] = background if grid[r][c] == color else color
    return output

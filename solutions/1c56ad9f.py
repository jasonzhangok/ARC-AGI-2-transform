from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    foreground = [(r, c) for r in range(height) for c in range(width) if grid[r][c] != background]
    bottom = max(r for r, _ in foreground)
    output = [[background] * width for _ in range(height)]
    for row, col in foreground:
        distance = bottom - row
        shift = -1 if distance % 4 == 1 else 1 if distance % 4 == 3 else 0
        output[row][col + shift] = grid[row][col]
    return output

from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    horizontal = [r for r, row in enumerate(grid) if all(value == 1 for value in row)]
    vertical = [c for c in range(width) if all(grid[r][c] == 1 for r in range(height))]
    colors = [value for row in grid for value in row if value not in (0, 1)]
    first, second = list(dict.fromkeys(colors))
    swap = {first: second, second: first}
    result = [row[:] for row in grid]
    cells = [(r, c, grid[r][c]) for r in range(height) for c in range(width) if grid[r][c] not in (0, 1)]
    for r, c, color in cells:
        result[r][c] = swap[color]
        if horizontal:
            rr, cc = 2 * horizontal[0] - r, c
        else:
            rr, cc = r, 2 * vertical[0] - c
        if 0 <= rr < height and 0 <= cc < width:
            result[rr][cc] = color
    return result

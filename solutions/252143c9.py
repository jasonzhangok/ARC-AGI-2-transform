def transform(grid):
    height, width = len(grid), len(grid[0])
    background = 7
    colors = set(value for row in grid for value in row) - {background}
    candidates = []
    for color in colors:
        pixels = [
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        ]
        top = min(row for row, _ in pixels)
        bottom = max(row for row, _ in pixels)
        left = min(col for _, col in pixels)
        right = max(col for _, col in pixels)
        candidates.append(((bottom - top + 1) * (right - left + 1), color,
                           top, bottom, left, right))
    _, color, top, bottom, left, right = max(candidates)
    output = [[background] * width for _ in range(height)]
    for offset in range(bottom - top + 1):
        output[top + offset][right - offset] = color
    return output

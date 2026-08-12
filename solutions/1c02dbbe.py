def transform(grid):
    height, width = len(grid), len(grid[0])
    fives = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5]
    top, bottom = min(r for r, _ in fives), max(r for r, _ in fives)
    left, right = min(c for _, c in fives), max(c for _, c in fives)
    colors = {value for row in grid for value in row if value not in (0, 5)}
    output = [[0 if value not in (0, 5) else value for value in row] for row in grid]
    for color in colors:
        points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == color]
        projected = [
            (min(max(r, top), bottom), min(max(c, left), right))
            for r, c in points
        ]
        r1, r2 = min(r for r, _ in projected), max(r for r, _ in projected)
        c1, c2 = min(c for _, c in projected), max(c for _, c in projected)
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                output[row][col] = color
    return output

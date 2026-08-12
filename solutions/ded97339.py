def transform(grid):
    output = [row[:] for row in grid]
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8]
    for r in {r for r, _ in points}:
        cols = [c for x, c in points if x == r]
        if len(cols) >= 2:
            for c in range(min(cols), max(cols) + 1):
                output[r][c] = 8
    for c in {c for _, c in points}:
        rows = [r for r, y in points if y == c]
        if len(rows) >= 2:
            for r in range(min(rows), max(rows) + 1):
                output[r][c] = 8
    return output

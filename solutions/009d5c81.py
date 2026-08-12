def transform(grid):
    marker = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 1
    ]
    top = min(r for r, _ in marker)
    left = min(c for _, c in marker)
    right = max(c for _, c in marker)
    top_width = sum(grid[top][c] == 1 for c in range(left, right + 1))

    if len(marker) == 5:
        replacement = 2
    elif top_width == 3:
        replacement = 7
    else:
        replacement = 3

    output = [
        [0 if value == 1 else replacement if value == 8 else value for value in row]
        for row in grid
    ]
    return output

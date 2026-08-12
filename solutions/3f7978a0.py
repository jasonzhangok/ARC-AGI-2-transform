def transform(grid):
    fives = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 5
    ]
    top = min(r for r, _ in fives) - 1
    bottom = max(r for r, _ in fives) + 1
    left = min(c for _, c in fives)
    right = max(c for _, c in fives)
    return [row[left : right + 1] for row in grid[top : bottom + 1]]

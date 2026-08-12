def transform(grid):
    height, width = len(grid), len(grid[0])
    markers = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    ]

    if len({col for _, col in markers}) == 1:
        half = height // 2
        selected = grid[:half] if all(row < half for row, _ in markers) else grid[half:]
    else:
        half = width // 2
        use_left = all(col < half for _, col in markers)
        selected = [row[:half] if use_left else row[half:] for row in grid]

    return [[8 if value == 5 else value for value in row] for row in selected]

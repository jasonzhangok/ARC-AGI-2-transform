def transform(grid):
    height, width = len(grid), len(grid[0])
    separator_row = next(r for r in range(height) if len(set(grid[r])) == 1 and grid[r][0] != 0)
    separator_color = grid[separator_row][0]
    separator_column = next(
        c for c in range(width)
        if all(grid[r][c] == separator_color for r in range(height))
    )
    regions = (
        (0, separator_row, 0, separator_column),
        (0, separator_row, separator_column + 1, width),
        (separator_row + 1, height, 0, separator_column),
        (separator_row + 1, height, separator_column + 1, width),
    )
    tiles = []
    for top, bottom, left, right in regions:
        points = [
            (r, c)
            for r in range(top, bottom)
            for c in range(left, right)
            if grid[r][c] not in (0, separator_color)
        ]
        r0, r1 = min(r for r, _ in points), max(r for r, _ in points)
        c0, c1 = min(c for _, c in points), max(c for _, c in points)
        tiles.append([grid[r][c0 : c1 + 1] for r in range(r0, r1 + 1)])

    output = [
        tiles[0][r] + tiles[1][r] for r in range(3)
    ] + [
        tiles[2][r] + tiles[3][r] for r in range(3)
    ]
    return output

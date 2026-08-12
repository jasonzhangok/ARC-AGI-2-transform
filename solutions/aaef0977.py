def transform(grid):
    cycle = [3, 4, 0, 5, 2, 8, 9, 6, 1]
    seed_row, seed_col = next(
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] != 7
    )
    start = cycle.index(grid[seed_row][seed_col])

    return [
        [
            cycle[
                (start + abs(row - seed_row) + abs(col - seed_col))
                % len(cycle)
            ]
            for col in range(len(grid[0]))
        ]
        for row in range(len(grid))
    ]

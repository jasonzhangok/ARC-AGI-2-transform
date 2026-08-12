def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    output = [row[:] for row in grid]

    ring = (
        (0, 0), (0, 1), (0, 2), (1, 2),
        (2, 2), (2, 1), (2, 0), (1, 0),
    )
    knight_order = (2, 7, 4, 1, 6, 3, 0, 5)
    for top in range(height - 2):
        for left in range(width - 2):
            if grid[top + 1][left + 1] != background:
                continue
            if not all(
                grid[top + row][left + col] != background
                for row, col in ring
            ):
                continue
            values = [grid[top + row][left + col] for row, col in ring]
            for target_index, source_index in enumerate(knight_order):
                row, col = ring[target_index]
                output[top + row][left + col] = values[source_index]

    return output

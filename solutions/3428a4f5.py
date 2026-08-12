def transform(grid):
    separator = next(r for r, row in enumerate(grid) if all(value == 4 for value in row))
    top = grid[:separator]
    bottom = grid[separator + 1:]
    return [
        [3 if (a != 0) != (b != 0) else 0 for a, b in zip(top_row, bottom_row)]
        for top_row, bottom_row in zip(top, bottom)
    ]

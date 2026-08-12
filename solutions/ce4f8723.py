def transform(grid):
    separator = next(r for r, row in enumerate(grid) if all(value == 4 for value in row))
    top = grid[:separator]
    bottom = grid[separator + 1:]
    output = [
        [3 if top[r][c] != 0 or bottom[r][c] != 0 else 0 for c in range(len(top[0]))]
        for r in range(len(top))
    ]
    return output

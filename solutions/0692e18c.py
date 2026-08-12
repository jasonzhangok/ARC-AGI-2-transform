def transform(grid):
    height, width = len(grid), len(grid[0])
    color = next(value for row in grid for value in row if value != 0)
    complement = [
        [color if value == 0 else 0 for value in row]
        for row in grid
    ]
    output = []
    for mask_row in grid:
        for pattern_row in complement:
            row = []
            for value in mask_row:
                row.extend(pattern_row if value != 0 else [0] * width)
            output.append(row)
    return output

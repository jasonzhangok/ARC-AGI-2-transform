def transform(grid):
    size = len(grid)
    left = [row[:size] for row in grid]
    right = [row[size:] for row in grid]

    def is_mask(panel):
        return all(value in (0, 8) for row in panel for value in row)

    if is_mask(left):
        mask, layout = left, right
    else:
        mask, layout = right, left

    output = [[0] * (size * size) for _ in range(size * size)]
    for macro_row in range(size):
        for macro_col in range(size):
            color = layout[macro_row][macro_col]
            if color == 0:
                continue
            for row in range(size):
                for col in range(size):
                    if mask[row][col] == 8:
                        output[macro_row * size + row][macro_col * size + col] = color
    return output

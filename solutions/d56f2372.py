def transform(grid):
    colors = sorted({value for row in grid for value in row if value != 0})
    for color in colors:
        cells = {
            (row, col)
            for row, line in enumerate(grid)
            for col, value in enumerate(line)
            if value == color
        }
        top = min(row for row, _ in cells)
        bottom = max(row for row, _ in cells)
        left = min(col for _, col in cells)
        right = max(col for _, col in cells)
        shape = {(row - top, col - left) for row, col in cells}
        width = right - left + 1
        if shape == {(row, width - 1 - col) for row, col in shape}:
            return [
                [color if (row, col) in cells else 0
                 for col in range(left, right + 1)]
                for row in range(top, bottom + 1)
            ]
    return []

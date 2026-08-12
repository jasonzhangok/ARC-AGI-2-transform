from collections import Counter


def transform(grid):
    result = [row[:] for row in grid]
    header_row = max(range(len(grid)), key=lambda r: sum(value != 0 for value in grid[r]))
    header = [(c, value) for c, value in enumerate(grid[header_row]) if value != 0]
    header_colors = {value for _, value in header}
    for column, color in header:
        markers = [
            (r, c)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value == color and (r, c) != (header_row, column)
        ]
        if not markers:
            markers = [(len(grid) - 1, column)]
        for marker_row, marker_col in markers:
            lo, hi = sorted((header_row, marker_row))
            for r in range(lo, hi + 1):
                result[r][column] = color
            lo, hi = sorted((column, marker_col))
            for c in range(lo, hi + 1):
                result[marker_row][c] = color
    return result

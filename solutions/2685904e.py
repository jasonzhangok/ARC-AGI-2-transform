from collections import Counter


def transform(grid):
    result = [row[:] for row in grid]
    separator = next(r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] == 5)
    count = sum(value == 8 for row in grid[:separator] for value in row)
    code_row = next(row for row in grid[separator + 1:] if any(value != 0 for value in row))
    frequencies = Counter(value for value in code_row if value != 0)
    selected = {color for color, frequency in frequencies.items() if frequency == count}
    for r in range(separator - count, separator):
        for c, color in enumerate(code_row):
            if color in selected:
                result[r][c] = color
    return result

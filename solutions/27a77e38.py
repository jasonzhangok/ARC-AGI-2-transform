from collections import Counter


def transform(grid):
    result = [row[:] for row in grid]
    separator = next(r for r, row in enumerate(grid) if all(value == 5 for value in row))
    counts = Counter(value for row in grid[:separator] for value in row)
    color = counts.most_common(1)[0][0]
    result[-1][len(grid[0]) // 2] = color
    return result

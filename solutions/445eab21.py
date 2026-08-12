from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row if value != 0)
    color = max(counts, key=counts.get)
    return [[color, color], [color, color]]

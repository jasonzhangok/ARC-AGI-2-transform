from collections import Counter


def transform(grid):
    keep = {color for color, _ in Counter(v for row in grid for v in row).most_common(2)}
    return [[v if v in keep else 7 for v in row] for row in grid]

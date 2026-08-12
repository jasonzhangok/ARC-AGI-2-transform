from collections import Counter


def transform(grid):
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    counts = Counter(value for row in grid for value in row if value != background)
    return [[color for color, _ in sorted(counts.items(), key=lambda item: (item[1], -item[0]))]]

from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row)
    colors = sorted(counts, key=lambda color: (-counts[color], color))
    height = counts[colors[0]]
    return [[color if r < counts[color] else 0 for color in colors] for r in range(height)]

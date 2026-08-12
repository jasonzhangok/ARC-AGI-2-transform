from collections import Counter


def transform(grid):
    """Straighten all foreground cells into a centered horizontal line."""
    height = len(grid)
    if height == 0:
        return []
    width = len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    foreground = [value for value in counts if value != background]

    output = [[background for _ in range(width)] for _ in range(height)]
    if not foreground:
        return output

    color = foreground[0]
    length = sum(value != background for row in grid for value in row)
    row = height // 2
    start = (width - length) // 2
    for column in range(start, start + length):
        output[row][column] = color
    return output

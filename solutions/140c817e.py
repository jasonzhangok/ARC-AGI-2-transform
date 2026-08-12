from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    marker = min((value for value in counts if value != background), key=counts.get)
    points = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == marker
    ]
    output = [row[:] for row in grid]

    for row, col in points:
        for x in range(width):
            output[row][x] = marker
        for y in range(height):
            output[y][col] = marker

    for row, col in points:
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            y, x = row + dr, col + dc
            if 0 <= y < height and 0 <= x < width and output[y][x] == background:
                output[y][x] = 3
        output[row][col] = 2
    return output

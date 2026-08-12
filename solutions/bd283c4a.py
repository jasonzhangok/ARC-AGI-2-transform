def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    first_seen = []
    for row in grid:
        for color in row:
            if color not in counts:
                counts[color] = 0
                first_seen.append(color)
            counts[color] += 1

    ranked = []
    for index, color in enumerate(first_seen):
        ranked.append((-counts[color], index, color))
    ranked.sort()

    result = [[0 for _ in range(width)] for _ in range(height)]
    position = 0
    for _, _, color in ranked:
        for _ in range(counts[color]):
            row = height - 1 - position % height
            column = position // height
            result[row][column] = color
            position += 1
    output = result
    return output

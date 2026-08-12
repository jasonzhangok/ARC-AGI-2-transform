def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    return [[value] for value in sorted(counts, key=lambda value: counts[value], reverse=True)]

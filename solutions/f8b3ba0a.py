def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    colors = sorted((value for value in counts if value != background),
                    key=lambda value: counts[value], reverse=True)
    return [[value] for value in colors]

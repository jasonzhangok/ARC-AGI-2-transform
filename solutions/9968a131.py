def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = 0
    background_count = -1
    for value in counts:
        if counts[value] > background_count:
            background = value
            background_count = counts[value]

    reference = []
    for row in grid:
        foreground = [value for value in row if value != background]
        if len(foreground) == 2:
            reference = foreground
            break

    output = []
    for row in grid:
        foreground = [value for value in row if value != background]
        if len(foreground) == 2 and foreground == reference[::-1]:
            output.append([row[-1]] + row[:-1])
        else:
            output.append(row[:])
    return output

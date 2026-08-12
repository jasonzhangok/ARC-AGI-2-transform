def transform(grid):
    output = [row[:] for row in grid]
    for row, line in enumerate(grid):
        guide_colors = {value for value in line if value not in (0, 5)}
        if not guide_colors:
            continue
        guide = next(iter(guide_colors))
        for col, value in enumerate(line):
            if value == 5:
                output[row][col] = guide
    return output

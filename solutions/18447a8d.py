def transform(grid):
    height, width = len(grid), len(grid[0])
    separators = [row for row in range(height) if all(value == 7 for value in grid[row])]
    bands = [(separators[i] + 1, separators[i + 1]) for i in range(len(separators) - 1)]
    data = []
    for top, bottom in bands:
        eight_counts = [sum(value == 8 for value in grid[row]) for row in range(top, bottom)]
        color = next(value for row in grid[top:bottom] for value in row if value not in (7, 8))
        color_counts = [sum(value == color for value in grid[row]) for row in range(top, bottom)]
        data.append((eight_counts, color, color_counts))

    output = [[7] * width for _ in range(height)]
    for row in separators:
        output[row] = [7] * width
    for index, (eight_counts, _, _) in enumerate(data):
        match = next(
            candidate
            for candidate in data
            if len(set(a + b for a, b in zip(eight_counts, candidate[2]))) == 1
        )
        color, color_counts = match[1], match[2]
        top, bottom = bands[index]
        for local_row, row in enumerate(range(top, bottom)):
            eight_cols = [col for col in range(width) if grid[row][col] == 8]
            for col in eight_cols:
                output[row][col] = 8
            start = max(eight_cols) + 1
            for col in range(start, start + color_counts[local_row]):
                output[row][col] = color
    return output

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    bars = []

    for row in range(height):
        for color in set(grid[row]) - {0}:
            runs = []
            column = 0
            while column < width:
                if grid[row][column] == color:
                    start = column
                    while column < width and grid[row][column] == color:
                        column += 1
                    runs.append((start, column - 1))
                else:
                    column += 1
            for index in range(len(runs) - 1):
                if runs[index + 1][0] - runs[index][1] == 2:
                    bars.append(
                        (
                            row,
                            color,
                            runs[index][0],
                            runs[index + 1][1],
                            runs[index][1] + 1,
                        )
                    )

    pivots = {}
    for row, color, left, right, pivot in bars:
        pivots.setdefault(pivot, []).append((row, color))

    output = [[0 for _ in range(width)] for _ in range(height)]
    for pivot, events in pivots.items():
        events.sort()
        bar_rows = {
            row
            for row, color, left, right, other_pivot in bars
            if left <= pivot <= right
        }
        seed_counts = {}
        for row in range(height):
            value = grid[row][pivot]
            if row not in bar_rows and value != 0:
                seed_counts[value] = seed_counts.get(value, 0) + 1
        seed = max(seed_counts, key=seed_counts.get)

        for row in range(height):
            color = seed
            for event_row, event_color in events:
                if event_row >= row:
                    color = event_color
                    break
            output[row][pivot] = color

    for row, color, left, right, pivot in bars:
        for column in range(left, right + 1):
            output[row][column] = color

    return output

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    best_period = 1
    best_mismatches = None

    for period in range(1, height // 2 + 1):
        mismatches = 0
        for phase in range(period):
            for col in range(width):
                counts = {}
                observed = 0
                for row in range(phase, height, period):
                    value = grid[row][col]
                    if value != 0:
                        counts[value] = counts.get(value, 0) + 1
                        observed += 1
                largest_count = 0
                for value in counts:
                    if counts[value] > largest_count:
                        largest_count = counts[value]
                mismatches += observed - largest_count
        if best_mismatches is None or mismatches < best_mismatches:
            best_mismatches = mismatches
            best_period = period

    pattern = []
    for phase in range(best_period):
        pattern_row = []
        for col in range(width):
            counts = {}
            for row in range(phase, height, best_period):
                value = grid[row][col]
                if value != 0:
                    counts[value] = counts.get(value, 0) + 1
            selected_value = 0
            selected_count = -1
            for value in counts:
                if counts[value] > selected_count:
                    selected_value = value
                    selected_count = counts[value]
            pattern_row.append(selected_value)
        pattern.append(pattern_row)

    output = []
    for row in range(height):
        output.append(pattern[row % best_period][:])
    return output

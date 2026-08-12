def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    bars = []
    for col in (0, width - 1):
        row = 0
        while row < height:
            if grid[row][col] != 2:
                row += 1
                continue
            start = row
            while row + 1 < height and grid[row + 1][col] == 2:
                row += 1
            bars.append((start, row, col))
            row += 1

    marked_index = None
    for index in range(len(bars)):
        start, end, col = bars[index]
        found = False
        for row in range(start, end + 1):
            for source_col in range(width):
                if grid[row][source_col] == 8:
                    found = True
        if found:
            marked_index = index

    marked_start, marked_end, marked_col = bars[marked_index]
    active_offsets = []
    for row in range(marked_start, marked_end + 1):
        marker = None
        for col in range(width):
            if grid[row][col] == 8:
                marker = col
                break
        if marker is not None:
            active_offsets.append(row - marked_start)
            if marked_col == 0:
                for col in range(1, marker):
                    output[row][col] = 8
            else:
                for col in range(marker + 1, width - 1):
                    output[row][col] = 8
            output[row][marker] = 4

    for index in range(len(bars)):
        if index == marked_index:
            continue
        start, end, col = bars[index]
        for offset in active_offsets:
            row = start + offset
            if row <= end:
                if col == 0:
                    for target_col in range(1, width):
                        output[row][target_col] = 8
                else:
                    for target_col in range(width - 1):
                        output[row][target_col] = 8

    return output

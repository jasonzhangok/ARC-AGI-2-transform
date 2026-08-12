def transform(grid):
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]

    eight_counts = [
        sum(value == 8 for value in grid[0]),
        sum(grid[row][width - 1] == 8 for row in range(height)),
        sum(value == 8 for value in grid[height - 1]),
        sum(grid[row][0] == 8 for row in range(height)),
    ]
    two_counts = [
        sum(value == 2 for value in grid[0]),
        sum(grid[row][width - 1] == 2 for row in range(height)),
        sum(value == 2 for value in grid[height - 1]),
        sum(grid[row][0] == 2 for row in range(height)),
    ]
    source_side = eight_counts.index(max(eight_counts))
    control_side = two_counts.index(max(two_counts))

    if source_side == 0:
        starts = [column for column in range(width) if grid[0][column] == 8]
    elif source_side == 2:
        starts = [
            column for column in range(width) if grid[height - 1][column] == 8
        ]
    elif source_side == 3:
        starts = [row for row in range(height) if grid[row][0] == 8]
    else:
        starts = [
            row for row in range(height) if grid[row][width - 1] == 8
        ]

    shift = 0
    if source_side == 0 or source_side == 2:
        shift_step = 1 if control_side == 3 else -1
        for depth in range(height):
            row = depth if source_side == 0 else height - 1 - depth
            marker = grid[row][0] if control_side == 3 else grid[row][width - 1]
            if marker == 2:
                shift += shift_step
            for start in starts:
                column = start + shift
                if 0 <= column < width and result[row][column] != 2:
                    result[row][column] = 8
    else:
        shift_step = 1 if control_side == 0 else -1
        for depth in range(width):
            column = depth if source_side == 3 else width - 1 - depth
            marker = grid[0][column] if control_side == 0 else grid[height - 1][column]
            if marker == 2:
                shift += shift_step
            for start in starts:
                row = start + shift
                if 0 <= row < height and result[row][column] != 2:
                    result[row][column] = 8

    output = result
    return output

def transform(grid):
    """Pack the checkerboard's blue cells toward the edge marked by 8."""
    height = len(grid)
    if height == 0:
        return []
    width = len(grid[0])

    marker_row, marker_col = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    )

    def packed_line(length, blue_count, special, toward_start):
        if special:
            line = (
                [8]
                + [1] * blue_count
                + [9] * blue_count
                + [0] * (length - 1 - 2 * blue_count)
            )
        else:
            line = [1] * blue_count + [0] * (length - blue_count)
        return line if toward_start else line[::-1]

    if marker_col == 0 or marker_col == width - 1:
        toward_start = marker_col == 0
        return [
            packed_line(
                width,
                sum(cell == 1 for cell in row),
                row_index == marker_row,
                toward_start,
            )
            for row_index, row in enumerate(grid)
        ]

    toward_start = marker_row == 0
    result = [[0 for _ in range(width)] for _ in range(height)]
    for col in range(width):
        blue_count = sum(grid[row][col] == 1 for row in range(height))
        packed = packed_line(
            height, blue_count, col == marker_col, toward_start
        )
        for row, color in enumerate(packed):
            result[row][col] = color
    return result

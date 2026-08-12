def transform(grid):
    pixels = [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 4
    ]
    top = min(row for row, _ in pixels)
    bottom = max(row for row, _ in pixels)
    left = min(col for _, col in pixels)
    right = max(col for _, col in pixels)
    pattern = [row[left:right + 1] for row in grid[top:bottom + 1]]
    pattern_height, pattern_width = len(pattern), len(pattern[0])
    transposed = [list(row) for row in zip(*pattern)]
    size = 2 * pattern_width + pattern_height
    output = [[0] * size for _ in range(size)]

    for row in range(pattern_height):
        for col in range(pattern_width):
            output[pattern_width + row][col] = pattern[row][col]
            output[pattern_width + row][pattern_width + pattern_height + col] = (
                pattern[row][pattern_width - 1 - col]
            )
    for row in range(pattern_width):
        for col in range(pattern_height):
            output[row][pattern_width + col] = transposed[row][col]
            output[pattern_width + pattern_height + row][pattern_width + col] = (
                transposed[pattern_width - 1 - row][col]
            )
    return output

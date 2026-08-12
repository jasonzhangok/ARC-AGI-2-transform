def transform(grid):
    size = len(grid)
    replacement = grid[0][0]
    pattern = [
        [replacement if value == 0 else value for value in row]
        for row in grid
    ]
    offset = int(any(value == 0 for row in grid for value in row))
    output = [[0] * (2 * size) for _ in range(2 * size)]
    for row in range(size):
        for col in range(size):
            output[row][col] = pattern[row][col]
            source_col = col + offset
            source_row = row + offset
            output[row][size + col] = (
                pattern[0][source_col] if source_col < size else replacement
            )
            output[size + row][col] = (
                pattern[source_row][0] if source_row < size else replacement
            )
            output[size + row][size + col] = (
                pattern[source_row][source_col]
                if source_row < size and source_col < size
                else replacement
            )
    return output

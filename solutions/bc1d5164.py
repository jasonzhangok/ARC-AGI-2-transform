def transform(grid):
    output = [[0] * 3 for _ in range(3)]
    corners = [
        (range(2), range(2), 0, 0),
        (range(2), range(len(grid[0]) - 2, len(grid[0])), 0, 1),
        (range(len(grid) - 2, len(grid)), range(2), 1, 0),
        (range(len(grid) - 2, len(grid)), range(len(grid[0]) - 2, len(grid[0])), 1, 1),
    ]
    for rows, cols, row_offset, col_offset in corners:
        for local_r, r in enumerate(rows):
            for local_c, c in enumerate(cols):
                if grid[r][c] != 0:
                    output[row_offset + local_r][col_offset + local_c] = grid[r][c]
    return output

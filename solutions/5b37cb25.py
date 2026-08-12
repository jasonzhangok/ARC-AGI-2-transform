def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = grid[1][1]
    output = [row[:] for row in grid]

    for row in range(2, height - 2):
        for col in range(2, width - 2):
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                pr, pc = -dc, dr
                cross = (
                    (row, col),
                    (row + dr, col + dc),
                    (row - dr, col - dc),
                    (row + pr, col + pc),
                    (row - pr, col - pc),
                )
                chevron = (
                    (row - 2 * dr, col - 2 * dc),
                    (row - dr + pr, col - dc + pc),
                    (row - dr - pr, col - dc - pc),
                    (row + 2 * pr, col + 2 * pc),
                    (row - 2 * pr, col - 2 * pc),
                )
                if (all(grid[r][c] == background for r, c in cross)
                        and all(1 <= r < height - 1 and 1 <= c < width - 1
                                for r, c in chevron)
                        and all(grid[r][c] != background for r, c in chevron)):
                    if dr == -1:
                        color = grid[0][1]
                    elif dr == 1:
                        color = grid[-1][1]
                    elif dc == -1:
                        color = grid[1][0]
                    else:
                        color = grid[1][-1]
                    for r, c in cross:
                        output[r][c] = color

    return output

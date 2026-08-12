def transform(grid):
    output = [[0] * 3 for _ in range(3)]
    output[1][1] = 5
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 5:
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    rr, cc = r + dr, c + dc
                    if (
                        0 <= rr < len(grid)
                        and 0 <= cc < len(grid[0])
                        and grid[rr][cc] not in (0, 5)
                    ):
                        output[dr + 1][dc + 1] = grid[rr][cc]
    return output

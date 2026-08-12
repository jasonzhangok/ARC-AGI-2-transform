def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 1:
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < height and 0 <= cc < width and output[rr][cc] == 0:
                        output[rr][cc] = 7
            elif value == 2:
                for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < height and 0 <= cc < width and output[rr][cc] == 0:
                        output[rr][cc] = 4
    return output

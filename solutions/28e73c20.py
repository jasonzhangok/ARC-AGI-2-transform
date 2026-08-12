def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [[0] * width for _ in range(height)]
    r = c = 0
    dr, dc = 0, 1
    result[r][c] = 3
    while True:
        moved = False
        for _ in range(2):
            nr, nc = r + dr, c + dc
            valid = 0 <= nr < height and 0 <= nc < width and result[nr][nc] == 0
            if valid:
                neighbors = ((nr - 1, nc), (nr + 1, nc), (nr, nc - 1), (nr, nc + 1))
                valid = all(
                    not (0 <= rr < height and 0 <= cc < width and result[rr][cc] == 3)
                    or (rr, cc) == (r, c)
                    for rr, cc in neighbors
                )
            if valid:
                r, c = nr, nc
                result[r][c] = 3
                moved = True
                break
            dr, dc = dc, -dr
        if not moved:
            break
    if height % 2 == 0 and width % 2 == 0:
        result[height // 2][width // 2 - 1] = 3
    output = result
    return output

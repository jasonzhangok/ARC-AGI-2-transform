def transform(grid):
    h, w = len(grid), len(grid[0])
    marks = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    red = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    center_r = (min(r for r, _ in marks) + max(r for r, _ in marks)) / 2
    center_c = (min(c for _, c in marks) + max(c for _, c in marks)) / 2
    red_r = (min(r for r, _ in red) + max(r for r, _ in red)) / 2
    red_c = (min(c for _, c in red) + max(c for _, c in red)) / 2
    dr, dc = round(center_r - red_r), round(center_c - red_c)
    out = [[0] * w for _ in range(h)]
    for r, c in marks: out[r][c] = 3
    for r, c in red: out[r + dr][c + dc] = 2
    output = out
    return output

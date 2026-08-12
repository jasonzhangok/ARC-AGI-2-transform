

def transform(grid):
    h, w = len(grid), len(grid[0])
    marker = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 5)
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] not in (0, 5)]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    pattern = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
    ph, pw = len(pattern), len(pattern[0])
    top = marker[0] - ph // 2
    left = marker[1] - pw // 2
    output = [row[:] for row in grid]
    output[marker[0]][marker[1]] = 0
    for r in range(ph):
        for c in range(pw):
            if pattern[r][c] != 0:
                output[top + r][left + c] = pattern[r][c]
    return output

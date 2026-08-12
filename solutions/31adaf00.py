def transform(grid):
    result = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    occupied = set()
    for size in range(min(height, width), 1, -1):
        for r in range(height - size + 1):
            for c in range(width - size + 1):
                square = {(rr, cc) for rr in range(r, r + size) for cc in range(c, c + size)}
                if not (square & occupied) and all(grid[rr][cc] == 0 for rr, cc in square):
                    occupied.update(square)
    for r, c in occupied:
        result[r][c] = 1
    output = result
    return output

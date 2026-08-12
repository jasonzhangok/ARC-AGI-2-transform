def transform(grid):
    h, w = len(grid), len(grid[0])

    def edge_count(dc):
        return sum(
            grid[r][c] == 5 and r + 1 < h and 0 <= c + dc < w
            and grid[r + 1][c + dc] == 5
            for r in range(h) for c in range(w)
        )

    sparse = min((-1, 1), key=edge_count)
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5:
                continue
            belongs_to_sparse = any(
                0 <= r + dr < h and 0 <= c + dr * sparse < w
                and grid[r + dr][c + dr * sparse] == 5
                for dr in (-1, 1)
            )
            out[r][c] = 2 if belongs_to_sparse else 8
    return out

def transform(grid):
    n = len(grid)
    counts = {}
    for cell_value in (v for row in grid for v in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    marker = min(((counts[_item_1], _index_1, _item_1) for _index_1, _item_1 in enumerate(counts)))[2]
    out = [[0] * (n * n) for _ in range(n * n)]
    for br in range(n):
        for bc in range(n):
            if grid[br][bc] != marker:
                continue
            for r in range(n):
                for c in range(n):
                    out[br * n + r][bc * n + c] = grid[r][c]
    output = out
    return output

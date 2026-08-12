def transform(grid):
    size = len(grid)
    k = next((n for n in range(1, size + 1) if n * n + n - 1 == size))
    tiles = []
    for br in range(k):
        for bc in range(k):
            tiles.append(tuple((tuple(grid[br * (k + 1) + r][bc * (k + 1):bc * (k + 1) + k]) for r in range(k))))
    clean = [tile for tile in tiles if all((v != 5 for row in tile for v in row))]
    motif = {}
    for cell_value in clean:
        motif[cell_value] = motif.get(cell_value, 0) + 1
    motif = max(motif, key=motif.get)
    counts = {}
    for cell_value in (v for row in motif for v in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    base = max(counts, key=counts.get)
    marker = next((v for v in counts if v != base))
    out = [[0] * size for _ in range(size)]
    for index, tile in enumerate(tiles):
        br, bc = divmod(index, k)
        stamp = sum((v == marker for row in tile for v in row)) > sum((v == base for row in tile for v in row))
        for r in range(k):
            for c in range(k):
                out[br * (k + 1) + r][bc * (k + 1) + c] = motif[r][c] if stamp else base
    output = out
    return output

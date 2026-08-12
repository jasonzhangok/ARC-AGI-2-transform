def transform(grid):
    h, w = len(grid), len(grid[0])
    cells = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8}
    candidates = []
    for r in range(h - 1):
        for c in range(w - 1):
            box = {(r,c), (r,c+1), (r+1,c), (r+1,c+1)}
            if box <= cells: candidates.append((1, box))
            for missing, color in (((r,c),2), ((r+1,c),3), ((r,c+1),4)):
                shape = box - {missing}
                if shape <= cells: candidates.append((color, shape))
    by_cell = {cell: [] for cell in cells}
    for candidate in candidates:
        for cell in candidate[1]: by_cell[cell].append(candidate)
    def cover(remaining):
        if not remaining: return []
        cell = min(remaining)
        options = [x for x in by_cell[cell] if x[1] <= remaining]
        options.sort(key=lambda x: (-len(x[1]), x[0]))
        for color, shape in options:
            rest = cover(remaining - shape)
            if rest is not None: return [(color, shape)] + rest
        return None
    pieces = cover(cells)
    out = [[0] * w for _ in range(h)]
    for color, shape in pieces:
        for r, c in shape: out[r][c] = color
    return out

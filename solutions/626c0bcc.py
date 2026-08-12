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
    stack = [(cells, [])]
    pieces = None
    while stack and pieces is None:
        remaining, selected = stack.pop()
        if not remaining:
            pieces = selected
            break
        cell = min(remaining)
        options = [x for x in by_cell[cell] if x[1] <= remaining]
        options = [record[2] for record in sorted(((-len(item[1]), item[0]), index, item) for index, item in enumerate(options))]
        for color, shape in reversed(options):
            stack.append((remaining - shape, selected + [(color, shape)]))
    out = [[0] * w for _ in range(h)]
    for color, shape in pieces:
        for r, c in shape: out[r][c] = color
    output = out
    return output

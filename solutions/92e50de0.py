def transform(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    lattice = None
    for value in counts:
        if lattice is None or counts[value] > counts[lattice]:
            lattice = value
    horizontal = {r for r in range(h) if all(value == lattice for value in grid[r])}
    vertical = {c for c in range(w) if all(grid[r][c] == lattice for r in range(h))}

    interval_sets = []
    for size, lines in ((h, horizontal), (w, vertical)):
        result = []
        start = 0
        for line in sorted(lines):
            if start < line:
                result.append((start, line))
            start = line + 1
        if start < size:
            result.append((start, size))
        interval_sets.append(result)
    row_cells, col_cells = interval_sets
    marks = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0, lattice)]
    sr = next(i for i, (a, b) in enumerate(row_cells) if any(a <= r < b for r, _, _ in marks))
    sc = next(i for i, (a, b) in enumerate(col_cells) if any(a <= c < b for _, c, _ in marks))
    ra, _ = row_cells[sr]
    ca, _ = col_cells[sc]
    motif = [(r - ra, c - ca, value) for r, c, value in marks]
    output = [row[:] for row in grid]
    for ri, (r0, r1) in enumerate(row_cells):
        for ci, (c0, c1) in enumerate(col_cells):
            if (ri - sr) % 2 == 0 and (ci - sc) % 2 == 0:
                for dr, dc, value in motif:
                    if r0 + dr < r1 and c0 + dc < c1:
                        output[r0 + dr][c0 + dc] = value
    return output

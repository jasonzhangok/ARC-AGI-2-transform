from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    lattice = Counter(value for row in grid for value in row if value != 0).most_common(1)[0][0]
    horizontal = {r for r in range(h) if all(value == lattice for value in grid[r])}
    vertical = {c for c in range(w) if all(grid[r][c] == lattice for r in range(h))}

    def intervals(size, lines):
        result = []
        start = 0
        for line in sorted(lines):
            if start < line:
                result.append((start, line))
            start = line + 1
        if start < size:
            result.append((start, size))
        return result

    row_cells = intervals(h, horizontal)
    col_cells = intervals(w, vertical)
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

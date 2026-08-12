def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen = set()
    regions = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2 or (r, c) in seen:
                continue
            st = [(r, c)]
            seen.add((r, c))
            cells = []
            while st:
                x, y = st.pop()
                cells.append((x, y))
                for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    q = (x + a, y + b)
                    if 0 <= q[0] < h and 0 <= q[1] < w and (q not in seen) and (grid[q[0]][q[1]] != 2):
                        seen.add(q)
                        st.append(q)
            regions.append(cells)
    fill = {}
    for cell_value in (v for row in grid for v in row if v not in (0, 2)):
        fill[cell_value] = fill.get(cell_value, 0) + 1
    fill = max(fill, key=fill.get)
    out = [[0] * w for _ in range(h)]
    for r, c in [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]:
        out[r][c] = 2
    target = next((cells for cells in regions if (h - 1, 0) in cells))
    for r, c in target:
        out[r][c] = fill
    output = out
    return output

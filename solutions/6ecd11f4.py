def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen = set()
    comps = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
            st = [(r, c)]
            seen.add((r, c))
            cells = []
            while st:
                x, y = st.pop()
                cells.append((x, y))
                for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    q = (x + a, y + b)
                    if 0 <= q[0] < h and 0 <= q[1] < w and (q not in seen) and (grid[q[0]][q[1]] == color):
                        seen.add(q)
                        st.append(q)
            comps.append((color, cells))
    big = max(((sum((len(x) for c, x in comps if c == _key_item_1 and len(x) > 1)), -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(set((c for c, _ in comps)))))[2]
    bp = set().union(*(set(x) for c, x in comps if c == big and len(x) > 1))
    br0, br1 = (min((r for r, c in bp)), max((r for r, c in bp)))
    bc0, bc1 = (min((c for r, c in bp)), max((c for r, c in bp)))
    small = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v != 0 and (r, c) not in bp]
    sr0, sr1 = (min((r for r, c in small)), max((r for r, c in small)))
    sc0, sc1 = (min((c for r, c in small)), max((c for r, c in small)))
    out = [[grid[r][c] for c in range(sc0, sc1 + 1)] for r in range(sr0, sr1 + 1)]
    oh, ow = (len(out), len(out[0]))
    bh = (br1 - br0 + 1) // oh
    bw = (bc1 - bc0 + 1) // ow
    for r in range(oh):
        for c in range(ow):
            if not any(((br0 + r * bh + i, bc0 + c * bw + j) in bp for i in range(bh) for j in range(bw))):
                out[r][c] = 0
    output = out
    return output

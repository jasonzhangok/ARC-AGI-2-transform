def transform(grid):
    try:
        h, w = (len(grid), len(grid[0]))
        seen = set()
        objects = []
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 0 or (r, c) in seen:
                    continue
                st = [(r, c)]
                seen.add((r, c))
                q = []
                while st:
                    x, y = st.pop()
                    q.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        p = (x + dx, y + dy)
                        if 0 <= p[0] < h and 0 <= p[1] < w and (p not in seen) and (grid[p[0]][p[1]] != 0):
                            seen.add(p)
                            st.append(p)
                objects.append(q)
        legends = [_rec1[2] for _rec1 in sorted(((min((c for r, c in _item1)), _idx1, _item1) for _idx1, _item1 in enumerate([q for q in objects if sum((grid[r][c] == 4 for r, c in q)) == 2])))]
        left = next((grid[r][c] for r, c in legends[0] if grid[r][c] != 4))
        right = next((grid[r][c] for r, c in legends[1] if grid[r][c] != 4))
        q = next((q for q in objects if q not in legends))
        r0, r1 = (min((r for r, c in q)), max((r for r, c in q)))
        c0, c1 = (min((c for r, c in q)), max((c for r, c in q)))
        crop = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
        result = []
        cur = crop
        for _ in range(4):
            for x in (cur, [row[::-1] for row in cur]):
                if x not in result:
                    result.append(x)
            cur = [list(row) for row in zip(*cur[::-1])]
        chosen = None
        for g in result:
            lv = [row[0] for row in g if row[0]]
            rv = [row[-1] for row in g if row[-1]]
            if lv and rv and (set(lv) == {left}) and (set(rv) == {right}):
                chosen = g
                break
        oh, ow = (len(chosen) + 2, len(chosen[0]) + 2)
        out = [[0] * ow for _ in range(oh)]
        out[0][0] = out[0][-1] = out[-1][0] = out[-1][-1] = 4
        for r, row in enumerate(chosen, 1):
            out[r][0] = left
            out[r][-1] = right
            out[r][1:-1] = row
        raise StopIteration(out)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output

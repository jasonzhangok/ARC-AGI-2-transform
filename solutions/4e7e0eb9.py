def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    split_rows = [r for r, row in enumerate(grid)
                  if len(set(row)) == 1 and row[0] not in (0, 4)]
    split_cols = [c for c in range(w)
                  if len({grid[r][c] for r in range(h)}) == 1
                  and grid[0][c] not in (0, 4)]

    def intervals(n, splits):
        b = [-1] + splits + [n]
        return [(b[i] + 1, b[i + 1]) for i in range(len(b) - 1) if b[i] + 1 < b[i + 1]]

    for r0, r1 in intervals(h, split_rows):
        for c0, c1 in intervals(w, split_cols):
            if r1 - r0 != 9 or c1 - c0 != 9:
                continue
            blocks = []
            for br in (1, 5):
                row = []
                for bc in (1, 5):
                    values = [grid[r0 + r][c0 + c]
                              for r in range(br, br + 3) for c in range(bc, bc + 3)]
                    row.append(max(set(values), key=values.count))
                blocks.append(row)
            flat = [v for row in blocks for v in row]
            non_one = [v for v in flat if v != 1]
            if len(non_one) == 1:
                new = [[non_one[0], non_one[0]], [non_one[0], non_one[0]]]
            elif all(grid[r0 + 4][c] == 4 for c in range(c0, c1)):
                new = [blocks[1], blocks[0]]
            elif all(grid[r][c0 + 4] == 4 for r in range(r0, r1)):
                new = [[row[1], row[0]] for row in blocks]
            else:
                new = blocks
            for bi, br in enumerate((1, 5)):
                for bj, bc in enumerate((1, 5)):
                    for r in range(br, br + 3):
                        for c in range(bc, bc + 3):
                            out[r0 + r][c0 + c] = new[bi][bj]
    return out

def transform(grid):
    h = len(grid)
    w = len(grid[0])
    output = []
    for _ in range(h * (h + 2)):
        output.append([0] * (w * (w + 2)))

    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == 0:
                continue
            macro_r = r + 1
            macro_c = c + 1
            for rr in range(macro_r * h, (macro_r + 1) * h):
                for cc in range(macro_c * w, (macro_c + 1) * w):
                    output[rr][cc] = color

            copies = []
            if r == 0:
                copies.append((0, c + 1))
            if r == h - 1:
                copies.append((h + 1, c + 1))
            if c == 0:
                copies.append((r + 1, 0))
            if c == w - 1:
                copies.append((r + 1, w + 1))
            for copy_r, copy_c in copies:
                for rr in range(h):
                    for cc in range(w):
                        output[copy_r * h + rr][copy_c * w + cc] = grid[rr][cc]
    return output

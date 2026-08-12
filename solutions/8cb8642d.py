def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    rectangles = []
    for r0 in range(h - 2):
        for r1 in range(r0 + 2, h):
            for c0 in range(w - 2):
                for c1 in range(c0 + 2, w):
                    border = ([grid[r0][c] for c in range(c0, c1 + 1)] +
                              [grid[r1][c] for c in range(c0, c1 + 1)] +
                              [grid[r][c0] for r in range(r0 + 1, r1)] +
                              [grid[r][c1] for r in range(r0 + 1, r1)])
                    base = border[0]
                    if base == 0 or any(value != base for value in border):
                        continue
                    inside = [grid[r][c] for r in range(r0 + 1, r1) for c in range(c0 + 1, c1)]
                    marks = {value for value in inside if value != base}
                    if len(marks) == 1 and 0 not in marks:
                        rectangles.append((r0, r1, c0, c1, base, marks.pop()))
    maximal = []
    for item in rectangles:
        r0, r1, c0, c1, _, _ = item
        if not any(a <= r0 and r1 <= b and x <= c0 and c1 <= y and (a, b, x, y) != (r0, r1, c0, c1)
                   for a, b, x, y, _, _ in rectangles):
            maximal.append(item)
    for r0, r1, c0, c1, base, mark in maximal:
        ih, iw = r1 - r0 - 1, c1 - c0 - 1
        for r in range(r0 + 1, r1):
            for c in range(c0 + 1, c1):
                output[r][c] = 0
        for i in range(ih):
            j = min(i, ih - 1 - i, (iw - 1) // 2)
            output[r0 + 1 + i][c0 + 1 + j] = mark
            output[r0 + 1 + i][c1 - 1 - j] = mark
            if ih <= iw and i == (ih - 1) // 2:
                for c in range(c0 + 1 + j, c1 - j):
                    output[r0 + 1 + i][c] = mark
    return output

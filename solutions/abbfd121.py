from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    best = None
    for color in {value for row in grid for value in row}:
        for top in range(h):
            valid = [True] * w
            for bottom in range(top, h):
                valid = [valid[c] and grid[bottom][c] == color for c in range(w)]
                c = 0
                while c < w:
                    if not valid[c]:
                        c += 1
                        continue
                    left = c
                    while c < w and valid[c]:
                        c += 1
                    candidate = ((bottom - top + 1) * (c - left),
                                 top, bottom, left, c - 1)
                    if best is None or candidate[0] > best[0]:
                        best = candidate
    _, top, bottom, left, right = best

    def row_agreement(shift):
        equal = sum(grid[r][c] == grid[r + shift][c]
                    for r in range(h - shift) for c in range(w))
        return equal / ((h - shift) * w)

    def column_agreement(shift):
        equal = sum(grid[r][c] == grid[r][c + shift]
                    for r in range(h) for c in range(w - shift))
        return equal / (h * (w - shift))

    row_period = max(range(1, h // 2 + 1), key=row_agreement)
    column_period = max(range(1, w // 2 + 1), key=column_agreement)
    pattern = {}
    for r in range(row_period):
        for c in range(column_period):
            values = [grid[nr][nc] for nr in range(h) for nc in range(w)
                      if nr % row_period == r and nc % column_period == c]
            pattern[r, c] = Counter(values).most_common(1)[0][0]
    return [[pattern[r % row_period, c % column_period]
             for c in range(left, right + 1)]
            for r in range(top, bottom + 1)]

def transform(grid):
    h, w = len(grid), len(grid[0])
    occupied = {(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0}
    candidates = []
    for top in range(h - 2):
        for left in range(w - 2):
            cells = {(r, c) for r in range(top, top + 3)
                     for c in range(left, left + 3)}
            if cells <= occupied:
                candidates.append((top, left, cells))

    solution = None

    def cover(remaining, selected):
        nonlocal solution
        if solution is not None:
            return
        if not remaining:
            solution = selected[:]
            return
        first = min(remaining)
        for candidate in candidates:
            if first in candidate[2] and candidate[2] <= remaining:
                cover(remaining - candidate[2], selected + [candidate])

    cover(occupied, [])
    out = [[5] * 9 for _ in range(9)]
    for top, left, _ in solution:
        tile = [row[left:left + 3] for row in grid[top:top + 3]]
        accents = [(r, c) for r in range(3) for c in range(3)
                   if tile[r][c] != 5]
        if accents:
            mean_r = sum(r for r, _ in accents) / len(accents)
            mean_c = sum(c for _, c in accents) / len(accents)
            target_r = min(range(3), key=lambda value: abs(value - mean_r))
            target_c = min(range(3), key=lambda value: abs(value - mean_c))
        else:
            target_r = target_c = 1
        for r in range(3):
            for c in range(3):
                out[target_r * 3 + r][target_c * 3 + c] = tile[r][c]
    return out

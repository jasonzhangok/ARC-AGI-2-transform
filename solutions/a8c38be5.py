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
    stack = [(occupied, [])]
    while stack and solution is None:
        remaining, selected = stack.pop()
        if not remaining:
            solution = selected
            break
        first = min(remaining)
        options = [candidate for candidate in candidates if first in candidate[2] and candidate[2] <= remaining]
        for candidate in reversed(options):
            stack.append((remaining - candidate[2], selected + [candidate]))
    out = [[5] * 9 for _ in range(9)]
    for top, left, _ in solution:
        tile = [row[left:left + 3] for row in grid[top:top + 3]]
        accents = [(r, c) for r in range(3) for c in range(3)
                   if tile[r][c] != 5]
        if accents:
            mean_r = sum(r for r, _ in accents) / len(accents)
            mean_c = sum(c for _, c in accents) / len(accents)
            target_r = min((abs(value - mean_r), value) for value in range(3))[1]
            target_c = min((abs(value - mean_c), value) for value in range(3))[1]
        else:
            target_r = target_c = 1
        for r in range(3):
            for c in range(3):
                out[target_r * 3 + r][target_c * 3 + c] = tile[r][c]
    output = out
    return output

def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid[6:]]
    reference = [(r, c) for r in range(6, h) for c in range(w) if grid[r][c] == 1]
    rr0, rr1 = min(r for r, _ in reference) - 6, max(r for r, _ in reference) - 6
    rc0, rc1 = min(c for _, c in reference), max(c for _, c in reference)
    payload_color = next(v for row in grid[:5] for v in row if v not in (0, 1, 2))
    payload = [(r, c) for r in range(5) for c in range(w) if grid[r][c] == payload_color]
    pr0, pr1 = min(r for r, _ in payload), max(r for r, _ in payload)
    pc0, pc1 = min(c for _, c in payload), max(c for _, c in payload)
    instruction_rows = [r for r in range(5) for c in range(w) if grid[r][c] == 2]
    bar_on_top = instruction_rows.count(min(instruction_rows)) >= 3
    target_r0 = rr1 + 1 if bar_on_top else rr0 - (pr1 - pr0 + 1)
    ref_center = (rc0 + rc1) // 2
    payload_center = (pc0 + pc1) // 2
    for r, c in payload:
        y = target_r0 + (r - pr0)
        x = ref_center + (c - payload_center)
        if 0 <= y < len(out) and 0 <= x < w:
            out[y][x] = payload_color
    return out

def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            if value:
                counts[value] = counts.get(value, 0) + 1

    frame = max(counts, key=counts.get)
    frame_cells = [(r, c) for r in range(h) for c in range(w)
                   if grid[r][c] == frame]
    top = min(r for r, _ in frame_cells)
    bottom = max(r for r, _ in frame_cells)
    left = min(c for _, c in frame_cells)
    right = max(c for _, c in frame_cells)
    middle_r = (top + bottom) / 2
    middle_c = (left + right) / 2

    markers = [(r, c, grid[r][c]) for r in range(top + 1, bottom)
               for c in range(left + 1, right)
               if grid[r][c] not in (0, frame)]
    for r, c, color in markers:
        out[r][c] = 0
        target_r = bottom + 1 if r < middle_r else top - 1
        target_c = right + 1 if c < middle_c else left - 1
        if 0 <= target_r < h and 0 <= target_c < w:
            out[target_r][target_c] = color
    return out

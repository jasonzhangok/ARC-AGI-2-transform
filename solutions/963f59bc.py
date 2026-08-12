def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    shape = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    top = min(r for r, _ in shape)
    bottom = max(r for r, _ in shape)
    left = min(c for _, c in shape)
    right = max(c for _, c in shape)
    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
               if grid[r][c] not in (0, 1)]

    for marker_r, marker_c, color in markers:
        if marker_c < left or marker_c > right:
            anchors = [(r, c) for r, c in shape if r == marker_r]
            anchor_r, anchor_c = min(
                anchors, key=lambda p: abs(p[1] - marker_c))
            reflected = [(r, left + right - c) for r, c in shape]
            reflected_anchor = (anchor_r, left + right - anchor_c)
        else:
            anchors = [(r, c) for r, c in shape if c == marker_c]
            anchor_r, anchor_c = min(
                anchors, key=lambda p: abs(p[0] - marker_r))
            reflected = [(top + bottom - r, c) for r, c in shape]
            reflected_anchor = (top + bottom - anchor_r, anchor_c)

        dr = marker_r - reflected_anchor[0]
        dc = marker_c - reflected_anchor[1]
        for r, c in reflected:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                out[nr][nc] = color
    return out

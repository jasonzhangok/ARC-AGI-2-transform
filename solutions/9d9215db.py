def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    reflected = {}
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if color == 0:
                continue
            for nr in (r, h - 1 - r):
                for nc in (c, w - 1 - c):
                    out[nr][nc] = color
                    reflected[(nr, nc)] = color

    for color in set(reflected.values()):
        cells = {position for position, value in reflected.items() if value == color}
        if len(cells) != 4:
            continue
        top = min(r for r, _ in cells)
        bottom = max(r for r, _ in cells)
        left = min(c for _, c in cells)
        right = max(c for _, c in cells)
        corners = {(top, left), (top, right), (bottom, left), (bottom, right)}
        if cells != corners or top == bottom or left == right:
            continue
        horizontal_hint = reflected.get((top, left + 2), 0)
        vertical_hint = reflected.get((top + 2, left), 0)
        if horizontal_hint == 0 or horizontal_hint != vertical_hint:
            continue
        edge_color = horizontal_hint
        for c in range(left + 2, right, 2):
            out[top][c] = edge_color
            out[bottom][c] = edge_color
        for r in range(top + 2, bottom, 2):
            out[r][left] = edge_color
            out[r][right] = edge_color
    output = out
    return output

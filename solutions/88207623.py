

def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    visited = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 2 or (r, c) in visited:
                continue
            run = []
            x = r
            while x < h and grid[x][c] == 2:
                run.append((x, c))
                visited.add((x, c))
                x += 1
            r0, r1 = run[0][0], run[-1][0]
            gray = [(x, y) for x in range(r0, r1 + 1) for y in range(w) if grid[x][y] == 4]
            left = [(x, y) for x, y in gray if y < c]
            right = [(x, y) for x, y in gray if y > c]
            source = left if len(left) > len(right) else right
            target_side = -1 if source is right else 1
            candidates = [grid[x][y] for x in range(r0, r1 + 1) for y in range(w)
                          if grid[x][y] not in (0, 2, 4) and (y - c) * target_side > 0]
            if not source or not candidates:
                continue
            marker = {}
            for cell_value in (candidates):
                marker[cell_value] = marker.get(cell_value, 0) + 1
            marker = max(marker, key=marker.get)
            for x, y in source:
                mirror = 2 * c - y
                if 0 <= mirror < w:
                    output[x][mirror] = marker
    return output

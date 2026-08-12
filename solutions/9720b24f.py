def _convex_hull(points):
    points = sorted(set((c, r) for r, c in points))
    if len(points) < 3:
        return points

    def cross(origin, a, b):
        return ((a[0] - origin[0]) * (b[1] - origin[1])
                - (a[1] - origin[1]) * (b[0] - origin[0]))

    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def _inside(point, polygon):
    if len(polygon) < 3:
        return False
    signs = []
    for a, b in zip(polygon, polygon[1:] + polygon[:1]):
        signs.append((b[0] - a[0]) * (point[1] - a[1])
                     - (b[1] - a[1]) * (point[0] - a[0]))
    return all(value >= 0 for value in signs) or all(value <= 0 for value in signs)


def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value != 0}
    hulls = {
        color: _convex_hull([(r, c) for r in range(h) for c in range(w)
                            if grid[r][c] == color])
        for color in colors
    }
    for r in range(h):
        for c in range(w):
            value = grid[r][c]
            if value and any(color != value and _inside((c, r), polygon)
                             for color, polygon in hulls.items()):
                out[r][c] = 0
    return out

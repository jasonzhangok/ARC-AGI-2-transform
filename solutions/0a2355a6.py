def transform(grid):
    output = [row[:] for row in grid]
    color_by_holes = {1: 1, 2: 3, 3: 2, 4: 4}
    _grid = grid
    height, width = len(_grid), len(_grid[0])
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if _grid[r][c] != 8 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            points = []
            while stack:
                y, x = stack.pop()
                points.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    yy, xx = y + dy, x + dx
                    if (
                        0 <= yy < height
                        and 0 <= xx < width
                        and (yy, xx) not in seen
                        and _grid[yy][xx] == 8
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append(points)
    _components_result_1 = result
    for points in _components_result_1:
        _points = points
        top, bottom = min(r for r, _ in _points), max(r for r, _ in _points)
        left, right = min(c for _, c in _points), max(c for _, c in _points)
        occupied = set(_points)
        seen = set()
        holes = 0
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if (r, c) in occupied or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                touches_edge = False
                while stack:
                    y, x = stack.pop()
                    if y in (top, bottom) or x in (left, right):
                        touches_edge = True
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        yy, xx = y + dy, x + dx
                        if (
                            top <= yy <= bottom
                            and left <= xx <= right
                            and (yy, xx) not in occupied
                            and (yy, xx) not in seen
                        ):
                            seen.add((yy, xx))
                            stack.append((yy, xx))
                if not touches_edge:
                    holes += 1
        _hole_count_result_2 = holes
        color = color_by_holes[_hole_count_result_2]
        for r, c in points:
            output[r][c] = color
    return output

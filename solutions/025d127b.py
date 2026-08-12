def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [[0] * width for _ in range(height)]

    _grid = grid
    height, width = len(_grid), len(_grid[0])
    directions = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    )
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if _grid[r][c] == 0 or (r, c) in seen:
                continue
            color = _grid[r][c]
            stack = [(r, c)]
            seen.add((r, c))
            points = []
            while stack:
                y, x = stack.pop()
                points.append((y, x))
                for dy, dx in directions:
                    yy, xx = y + dy, x + dx
                    if (
                        0 <= yy < height
                        and 0 <= xx < width
                        and (yy, xx) not in seen
                        and _grid[yy][xx] == color
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append((color, points))
    _components_result_1 = result
    for color, points in _components_result_1:
        right_edge = max(c for _, c in points)
        rows = {}
        for r, c in points:
            rows.setdefault(r, []).append(c)

        for r, columns in rows.items():
            columns.sort()
            runs = [[columns[0]]]
            for c in columns[1:]:
                if c == runs[-1][-1] + 1:
                    runs[-1].append(c)
                else:
                    runs.append([c])
            for run in runs:
                shift = 1 if run[-1] < right_edge else 0
                for c in run:
                    output[r][c + shift] = color

    return output

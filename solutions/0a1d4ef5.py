def transform(grid):
    _grid = grid
    height, width = (len(_grid), len(_grid[0]))
    seen = set()
    rectangles = []
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
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    yy, xx = (y + dy, x + dx)
                    if 0 <= yy < height and 0 <= xx < width and ((yy, xx) not in seen) and (_grid[yy][xx] == color):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            top, bottom = (min((y for y, _ in points)), max((y for y, _ in points)))
            left, right = (min((x for _, x in points)), max((x for _, x in points)))
            area = (bottom - top + 1) * (right - left + 1)
            if len(points) >= 9 and len(points) == area:
                rectangles.append((top, bottom, left, right, color))
    _solid_rectangles_result_1 = rectangles
    rectangles = sorted(_solid_rectangles_result_1)
    rows = []
    for rectangle in rectangles:
        top, bottom = (rectangle[0], rectangle[1])
        if not rows or top > rows[-1][0]:
            rows.append([bottom, [rectangle]])
        else:
            rows[-1][0] = max(rows[-1][0], bottom)
            rows[-1][1].append(rectangle)
    output = [[rectangle[4] for rectangle in [_record_1[2] for _record_1 in sorted(((_item_1[2], _index_1, _item_1) for _index_1, _item_1 in enumerate(row)))]] for _, row in rows]
    return output

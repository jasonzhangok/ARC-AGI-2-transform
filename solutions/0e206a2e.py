def transform(grid):
    height, width = len(grid), len(grid[0])
    _grid = grid
    height, width = len(_grid), len(_grid[0])
    directions = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr, dc) != (0, 0)
    ]
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if _grid[r][c] == 0 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            points = []
            while stack:
                y, x = stack.pop()
                points.append((y, x, _grid[y][x]))
                for dy, dx in directions:
                    yy, xx = y + dy, x + dx
                    if (
                        0 <= yy < height
                        and 0 <= xx < width
                        and (yy, xx) not in seen
                        and _grid[yy][xx] != 0
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append(points)
    _components_result_1 = result
    components = _components_result_1
    objects = [component for component in components if len(component) >= 5]
    anchors = [
        point
        for component in components
        if len(component) < 5
        for point in component
    ]
    output = [[0] * width for _ in range(height)]

    for obj in objects:
        best = None
        _points = obj
        variants = []
        for reflected in (False, True):
            current = [(r, -c if reflected else c, color) for r, c, color in _points]
            for _ in range(4):
                top = min(r for r, _, _ in current)
                left = min(c for _, c, _ in current)
                normalized = tuple(sorted((r - top, c - left, color) for r, c, color in current))
                if normalized not in variants:
                    variants.append(normalized)
                current = [(c, -r, color) for r, c, color in current]
        _variants_result_2 = variants
        for pattern in _variants_result_2:
            for anchor_r, anchor_c, anchor_color in anchors:
                for pattern_r, pattern_c, pattern_color in pattern:
                    if pattern_color != anchor_color:
                        continue
                    dr, dc = anchor_r - pattern_r, anchor_c - pattern_c
                    stamp = {
                        (r + dr, c + dc): color
                        for r, c, color in pattern
                    }
                    if not all(0 <= r < height and 0 <= c < width for r, c in stamp):
                        continue
                    score = sum(
                        stamp.get((r, c)) == color
                        for r, c, color in anchors
                    )
                    if best is None or score > best[0]:
                        best = (score, stamp)
        for (r, c), color in best[1].items():
            output[r][c] = color
    return output

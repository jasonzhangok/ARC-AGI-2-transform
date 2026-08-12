def _components(grid):
    height, width = len(grid), len(grid[0])
    directions = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    )
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
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
                        and grid[yy][xx] != 0
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append(points)
    return result


def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [[0] * width for _ in range(height)]
    for points in _components(grid):
        center_r = (min(r for r, _ in points) + max(r for r, _ in points)) // 2
        center_c = (min(c for _, c in points) + max(c for _, c in points)) // 2
        center_color = grid[center_r][center_c]
        arm_color = next(
            grid[r][c] for r, c in points if grid[r][c] != center_color
        )
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                rr, cc = center_r + dr, center_c + dc
                if not (0 <= rr < height and 0 <= cc < width):
                    continue
                if abs(dr) == abs(dc):
                    output[rr][cc] = center_color
                elif dr == 0 or dc == 0:
                    output[rr][cc] = arm_color
    return output

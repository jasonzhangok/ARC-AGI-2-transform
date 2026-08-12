def transform(grid):
    height, width = len(grid), len(grid[0])
    panels = []
    for top in range(height - 4):
        for left in range(width - 4):
            color = grid[top][left]
            if color == 0:
                continue
            border = [grid[top][c] for c in range(left, left + 5)]
            border += [grid[top + 4][c] for c in range(left, left + 5)]
            border += [grid[r][left] for r in range(top + 1, top + 4)]
            border += [grid[r][left + 4] for r in range(top + 1, top + 4)]
            if all(value == color for value in border):
                panels.append((top, left, color))

    by_color = {}
    for top, left, color in panels:
        mask = {
            (dr, dc)
            for dr in range(1, 4)
            for dc in range(1, 4)
            if grid[top + dr][left + dc] == color
        }
        by_color.setdefault(color, []).append((top, left, mask))

    result = [row[:] for row in grid]
    for color, items in by_color.items():
        template = max((mask for _, _, mask in items), key=len)
        for top, left, _ in items:
            for dr, dc in template:
                result[top + dr][left + dc] = color
    output = result
    return output

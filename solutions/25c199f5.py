def transform(grid):
    height, width = len(grid), len(grid[0])
    separators = [c for c in range(width) if all(grid[r][c] == 6 for r in range(height))]
    cuts = [-1] + separators + [width]
    panels = [(cuts[i] + 1, cuts[i + 1]) for i in range(len(cuts) - 1)]
    result = [[7] * (panels[0][1] - panels[0][0]) for _ in range(height)]

    bottom = height
    for left, right in panels:
        cells = {
            (r, c - left, grid[r][c])
            for r in range(height)
            for c in range(left, right)
            if grid[r][c] != 7
        }
        if not cells:
            continue
        top = min(r for r, _, _ in cells)
        object_bottom = max(r for r, _, _ in cells)
        object_height = object_bottom - top + 1
        delta = bottom - object_height - top
        for r, c, color in cells:
            result[r + delta][c] = color
        bottom -= object_height
    return result

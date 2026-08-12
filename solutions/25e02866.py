def transform(grid):
    height, width = (len(grid), len(grid[0]))
    counts = {}
    for cell_value in (value for row in grid for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    background = max(counts, key=counts.get)
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = list([start])
        while queue:
            r, c = queue.pop(0)
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (rr, cc) in remaining:
                    remaining.remove((rr, cc))
                    component.add((rr, cc))
                    queue.append((rr, cc))
        components.append(component)
    base = {}
    for cell_value in (grid[r][c] for comp in components for r, c in comp):
        base[cell_value] = base.get(cell_value, 0) + 1
    base = max(base, key=base.get)
    boxes = []
    for comp in components:
        rows = [r for r, _ in comp]
        cols = [c for _, c in comp]
        boxes.append((min(rows), max(rows), min(cols), max(cols)))
    out_h = boxes[0][1] - boxes[0][0] + 1
    out_w = boxes[0][3] - boxes[0][2] + 1
    result = [[base] * out_w for _ in range(out_h)]
    for top, bottom, left, right in boxes:
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if grid[r][c] != base:
                    result[r - top][c - left] = grid[r][c]
    output = result
    return output

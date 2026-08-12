

def transform(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for cell_value in (value for row in grid for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    background = max(counts, key=counts.get)
    colors = [value for value in counts if value != background]
    boxes = []
    for color in colors:
        cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color]
        boxes.append((min(r for r, _ in cells), max(r for r, _ in cells), min(c for _, c in cells), max(c for _, c in cells), color))
    output = [row[:] for row in grid]
    a, b = boxes
    if a[3] < b[2] or b[3] < a[2]:
        if b[3] < a[2]:
            a, b = b, a
        gap = list(range(a[3] + 1, b[2]))
        half = len(gap) // 2
        for c in gap[:half]:
            for r in range(h):
                output[r][c] = a[4]
        for c in gap[len(gap) - half:]:
            for r in range(h):
                output[r][c] = b[4]
    else:
        if b[1] < a[0]:
            a, b = b, a
        gap = list(range(a[1] + 1, b[0]))
        half = len(gap) // 2
        for r in gap[:half]:
            output[r] = [a[4]] * w
        for r in gap[len(gap) - half:]:
            output[r] = [b[4]] * w
    return output

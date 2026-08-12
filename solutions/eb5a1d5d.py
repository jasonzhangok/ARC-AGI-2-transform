def transform(grid):
    colors = set(v for row in grid for v in row)
    boxes = []
    for color in colors:
        cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row)
                 if v == color]
        r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
        c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
        boxes.append(((r1 - r0 + 1) * (c1 - c0 + 1), color))
    layers = [color for _, color in sorted(boxes, reverse=True)]
    n = len(layers)
    size = 2 * n - 1
    return [[layers[min(r, c, size - 1 - r, size - 1 - c)]
             for c in range(size)] for r in range(size)]

def transform(grid):
    height, width = len(grid), len(grid[0])
    legend = []
    legend_cells = set()
    for r, row in enumerate(grid):
        if row[0] != 0 and row[1] != 0:
            legend.append((row[0], row[1]))
            legend_cells.update(((r, 0), (r, 1)))
    boxes = []
    for source, fill in legend:
        cells = [(r, c) for r in range(height) for c in range(width) if (r, c) not in legend_cells and grid[r][c] == source]
        top = min(r for r, _ in cells) - 1
        bottom = max(r for r, _ in cells) + 1
        left = min(c for _, c in cells) - 1
        right = max(c for _, c in cells) + 1
        boxes.append((top, bottom, left, right, source, fill, cells))
    result = [[0] * width for _ in range(height)]
    for top, bottom, left, right, source, fill, cells in sorted(boxes):
        for r in range(max(0, top), min(height - 1, bottom) + 1):
            for c in range(max(0, left), min(width - 1, right) + 1):
                result[r][c] = fill
    for _, _, _, _, source, _, cells in boxes:
        for r, c in cells:
            result[r][c] = source
    return result

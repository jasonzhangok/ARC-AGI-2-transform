def transform(grid):
    colors = [value for row in grid for value in row if value not in (0, 5)]
    unique = []
    for value in colors:
        if value not in unique:
            unique.append(value)
    positions = {color: [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color]
                 for color in unique}
    vertical = all(max(r for r, _ in cells) - min(r for r, _ in cells) >=
                   max(c for _, c in cells) - min(c for _, c in cells) for cells in positions.values())
    key = (lambda color: min(c for _, c in positions[color])) if vertical else (lambda color: min(r for r, _ in positions[color]))
    ordered = sorted(unique, key=key)
    n = len(ordered)
    if vertical:
        return [ordered[:] for _ in range(n)]
    return [[color] * n for color in ordered]

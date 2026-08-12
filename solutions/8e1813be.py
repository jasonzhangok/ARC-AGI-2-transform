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
    if vertical:
        ordered = [item[2] for item in sorted((min(c for _, c in positions[color]), index, color) for index, color in enumerate(unique))]
    else:
        ordered = [item[2] for item in sorted((min(r for r, _ in positions[color]), index, color) for index, color in enumerate(unique))]
    n = len(ordered)
    if vertical:
        output = [ordered[:] for _ in range(n)]
    else:
        output = [[color] * n for color in ordered]
    return output

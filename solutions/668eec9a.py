def transform(grid):
    colors = sorted(
        set(v for row in grid for v in row) - {7},
        key=lambda color: min(r for r, row in enumerate(grid) if color in row),
    )
    colors = [7] * (5 - len(colors)) + colors
    return [[color] * 3 for color in colors]

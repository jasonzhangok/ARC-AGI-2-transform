def transform(grid):
    divider = {}
    for cell_value in (v for row in grid for v in row if v):
        divider[cell_value] = divider.get(cell_value, 0) + 1
    divider = max(divider, key=divider.get)
    counts = {}
    for cell_value in (v for row in grid for v in row if v not in (0, divider)):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    counts = {color: n // 4 for color, n in counts.items()}
    items = sorted(((n, c) for c, n in counts.items()))
    width = max((n for n, c in items))
    output = [[c] * n + [0] * (width - n) for n, c in items]
    return output

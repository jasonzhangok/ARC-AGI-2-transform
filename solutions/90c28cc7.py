def transform(grid):
    signatures = []
    widths = []
    for row in grid:
        runs = []
        c = 0
        while c < len(row):
            if row[c] == 0:
                c += 1
                continue
            color = row[c]
            end = c
            while end < len(row) and row[end] == color:
                end += 1
            runs.append((color, end - c))
            widths.append(end - c)
            c = end
        if runs and (not signatures or runs != signatures[-1]):
            signatures.append(runs)
    unit = min(widths)
    output = [[color for color, width in runs for _ in range(max(1, width // unit))]
            for runs in signatures]
    return output

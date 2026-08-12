def transform(grid):
    n = len(grid)
    bg = 5
    zero = [0] * n
    out = []
    for row in grid:
        blocks = [grid if v == bg else [zero] * n for v in row]
        for i in range(n):
            out.append(sum((block[i] for block in blocks), []))
    output = out
    return output

def transform(grid):
    output = []
    for row in grid:
        left = row[:6]
        right = row[7:13]
        output.append([1 if a == 7 or b == 7 else 0 for a, b in zip(left, right)])
    return output

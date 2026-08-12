def transform(grid):
    output = []
    for row in grid:
        left, right = row[:3], row[4:]
        output.append([8 if a == 0 and b == 0 else 0 for a, b in zip(left, right)])
    return output

def transform(grid):
    values = [
        value
        for _, _, value in sorted(
            (c, r, value)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value != 0
        )
    ]
    output = []
    for start in range(0, 9, 3):
        row = values[start:start + 3]
        if (start // 3) % 2 == 1:
            row.reverse()
        output.append(row + [0] * (3 - len(row)))
    return output

def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    dominant = max(counts, key=counts.get)
    output = [[0 for _ in range(3)] for _ in range(3)]

    if dominant % 2 == 0:
        for col in range(3):
            output[1][col] = 8
    else:
        output[0][2] = 8
        output[1][1] = 8
        output[2][1] = 8
        output[(3 - dominant) // 2][(dominant - 1) // 2] = 8
    return output

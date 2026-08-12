def transform(grid):
    output = [grid[0][:]]
    for _ in range(1, len(grid)):
        previous = output[-1]
        row = [7] * len(previous)
        for c in range(1, len(previous) - 1):
            left, right = previous[c - 1], previous[c + 1]
            if left == 7 or right == 7:
                continue
            if left == right:
                row[c] = 5 if left == 2 else 2
            else:
                row[c] = right
        output.append(row)
    return output

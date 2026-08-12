def transform(grid):
    header = grid[0]
    output = [header[:], grid[1][:]]
    for r in range(2, len(grid)):
        output.append([header[(r - 2) % len(header)]] * len(header))
    return output

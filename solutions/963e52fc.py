def transform(grid):
    width = len(grid[0])
    output = []
    for row in grid:
        period = width
        for p in range(1, width + 1):
            if all(row[c] == row[c % p] for c in range(width)):
                period = p
                break
        motif = row[:period]
        output.append([motif[c % period] for c in range(2 * width)])
    return output

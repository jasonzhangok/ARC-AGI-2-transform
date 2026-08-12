def transform(grid):
    height, width = (len(grid), len(grid[0]))
    candidates = []
    for row_period in range(1, height + 1):
        for col_period in range(1, width + 1):
            buckets = {}
            valid = True
            for row in range(height):
                for col in range(width):
                    value = grid[row][col]
                    if value == 0:
                        continue
                    key = (row % row_period, col % col_period)
                    if key in buckets and buckets[key] != value:
                        valid = False
                        break
                    buckets[key] = value
                if not valid:
                    break
            if valid and len(buckets) == row_period * col_period:
                candidates.append((row_period * col_period, row_period, col_period, buckets))
    _, row_period, col_period, pattern = min(candidates)
    output = [[pattern[row % row_period, col % col_period] for col in range(width)] for row in range(height)]
    return output

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = grid[height - 1][width - 1]

    best_rules = []
    best_cells = set()
    for left in range(width - 1):
        row = 0
        while row < height:
            if (grid[row][left] == background
                    or grid[row][left + 1] == background):
                row += 1
                continue
            start = row
            rules = []
            while row < height:
                if (grid[row][left] == background
                        or grid[row][left + 1] == background):
                    break
                rules.append((grid[row][left], grid[row][left + 1]))
                row += 1
            if len(rules) > len(best_rules):
                best_rules = rules
                best_cells = set((rule_row, column)
                                 for rule_row in range(start, row)
                                 for column in (left, left + 1))

    output = [row[:] for row in grid]
    for source, target in best_rules:
        for row in range(height):
            for column in range(width):
                if (row, column) not in best_cells and output[row][column] == source:
                    output[row][column] = target
    return output

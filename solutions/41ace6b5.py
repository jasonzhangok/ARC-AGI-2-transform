def transform(grid):
    result = [row[:] for row in grid]

    divider = 0
    for r in range(len(grid)):
        if 2 in grid[r]:
            divider = r
            break

    count_eight = 0
    for c in range(len(grid[0])):
        if grid[divider][c] != 2:
            current_eight = 0
            for r in range(len(grid)):
                if grid[r][c] == 8:
                    current_eight += 1
            if current_eight > count_eight:
                count_eight = current_eight

    for c in range(len(grid[0])):
        if grid[divider][c] != 2:
            count_one = 0
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    count_one += 1

            for r in range(len(grid)):
                if r < divider - count_eight + 1:
                    result[r][c] = 7
                elif r <= divider:
                    result[r][c] = 8
                elif r <= divider + count_one:
                    result[r][c] = 1
                else:
                    result[r][c] = 9

    return result

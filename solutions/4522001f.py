def transform(grid):
    colored = []
    red_row = 0
    red_col = 0
    green_count = 0
    for row in range(3):
        for col in range(3):
            if grid[row][col] != 0:
                colored.append((row, col))
            if grid[row][col] == 2:
                red_row = row
                red_col = col
            elif grid[row][col] == 3:
                green_count += 1
    top = min(row for row, col in colored)
    left = min(col for row, col in colored)
    bottom = max(row for row, col in colored)
    right = max(col for row, col in colored)
    side = green_count + 1
    starts = []
    if (red_row, red_col) in ((top, left), (bottom, right)):
        starts = [(top, left), (top + side, left + side)]
    else:
        starts = [(top, left + side), (top + side, left)]
    output = [[0 for col in range(9)] for row in range(9)]
    for block_top, block_left in starts:
        for row in range(block_top, block_top + side):
            for col in range(block_left, block_left + side):
                if 0 <= row < 9 and 0 <= col < 9:
                    output[row][col] = 3
    return output

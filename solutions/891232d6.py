def transform(grid):
    result = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0])

    for start_col in range(width):
        if grid[height - 1][start_col] != 6:
            continue

        col = start_col
        for row in range(height - 2, -1, -1):
            if (
                row > 0
                and 0 < col < width - 1
                and grid[row][col] != 7
                and grid[row - 1][col] == 7
                and grid[row][col - 1] == 7
                and grid[row][col + 1] == 7
            ):
                result[row][col] = 6
                break

            if grid[row][col] == 7:
                right = col
                while right + 1 < width and grid[row][right + 1] == 7:
                    right += 1

                result[row][col] = 8
                result[row + 1][col] = 4
                for detour_col in range(col + 1, right + 1):
                    result[row + 1][detour_col] = 2

                if right + 1 < width:
                    result[row + 1][right + 1] = 3
                col = right + 1

                if col >= width:
                    break

                if (
                    row > 0
                    and col < width - 1
                    and grid[row - 1][col] == 7
                    and grid[row][col - 1] == 7
                    and grid[row][col + 1] == 7
                ):
                    result[row][col] = 6
                    break

            result[row][col] = 6 if row == 0 else 2

    output = result
    return output

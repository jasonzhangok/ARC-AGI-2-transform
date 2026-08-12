def transform(grid):
    seen = set()
    count = 0
    for start_row in range(len(grid)):
        for start_col in range(len(grid[0])):
            if grid[start_row][start_col] != 2 or (start_row, start_col) in seen:
                continue
            count += 1
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    cell = (row + drow, col + dcol)
                    if (
                        0 <= cell[0] < len(grid)
                        and 0 <= cell[1] < len(grid[0])
                        and grid[cell[0]][cell[1]] == 2
                        and cell not in seen
                    ):
                        seen.add(cell)
                        queue.append(cell)
    output = [[0, 0, 0] for _ in range(3)]
    order = ((0, 0), (0, 2), (1, 1), (2, 0), (2, 2))
    for row, col in order[:count]:
        output[row][col] = 1
    return output

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    squares = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 9 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor_row = current_row + row_step
                    neighbor_col = current_col + col_step
                    neighbor = (neighbor_row, neighbor_col)
                    if (0 <= neighbor_row < height and 0 <= neighbor_col < width
                            and grid[neighbor_row][neighbor_col] == 9
                            and neighbor not in seen):
                        seen.add(neighbor)
                        stack.append(neighbor)

            top = min(cell[0] for cell in cells)
            bottom = max(cell[0] for cell in cells)
            left = min(cell[1] for cell in cells)
            right = max(cell[1] for cell in cells)
            side = max(bottom - top + 1, right - left + 1)
            if bottom - top + 1 < side:
                if top == 0:
                    top = bottom - side + 1
                else:
                    bottom = top + side - 1
            if right - left + 1 < side:
                if left == 0:
                    left = right - side + 1
                else:
                    right = left + side - 1
            squares.append((top, bottom, left, right, side))

    output = [row[:] for row in grid]
    for top, bottom, left, right, side in squares:
        thickness = side // 2
        outer_bottom = bottom + thickness
        for row in range(max(0, outer_bottom + 1), height):
            for col in range(max(0, left), min(width, right + 1)):
                if grid[row][col] == 0:
                    output[row][col] = 1

    for top, bottom, left, right, side in squares:
        thickness = side // 2
        for row in range(max(0, top - thickness),
                         min(height, bottom + thickness + 1)):
            for col in range(max(0, left - thickness),
                             min(width, right + thickness + 1)):
                if (not (top <= row <= bottom and left <= col <= right)
                        and grid[row][col] != 9):
                    output[row][col] = 3
    return output

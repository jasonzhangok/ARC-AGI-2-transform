def transform(grid):
    """Complete every azure component to its smallest enclosing diamond."""
    result = [row[:] for row in grid]
    if not grid or not grid[0]:
        return result

    height = len(grid)
    width = len(grid[0])
    seen = set()
    diamonds = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != 8:
                continue
            if (start_row, start_col) in seen:
                continue

            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            component = []

            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = row + drow
                    next_col = col + dcol
                    neighbor = (next_row, next_col)
                    if not (0 <= next_row < height and 0 <= next_col < width):
                        continue
                    if neighbor in seen or grid[next_row][next_col] != 8:
                        continue
                    seen.add(neighbor)
                    stack.append(neighbor)

            diagonal_sum = [row + col for row, col in component]
            diagonal_difference = [row - col for row, col in component]
            diamonds.append(
                (
                    min(diagonal_sum),
                    max(diagonal_sum),
                    min(diagonal_difference),
                    max(diagonal_difference),
                )
            )

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                continue
            diagonal_sum = row + col
            diagonal_difference = row - col
            if any(
                min_sum <= diagonal_sum <= max_sum
                and min_difference <= diagonal_difference <= max_difference
                for min_sum, max_sum, min_difference, max_difference in diamonds
            ):
                result[row][col] = 4

    return result

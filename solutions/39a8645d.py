from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    patterns = []
    for color in {value for row in grid for value in row if value not in (0, 2)}:
        seen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                component = []
                stack = [(row, col)]
                seen.add((row, col))
                while stack:
                    current_row, current_col = stack.pop()
                    component.append((current_row, current_col))
                    for row_step in (-1, 0, 1):
                        for col_step in (-1, 0, 1):
                            next_row = current_row + row_step
                            next_col = current_col + col_step
                            next_cell = (next_row, next_col)
                            if (
                                0 <= next_row < height
                                and 0 <= next_col < width
                                and next_cell not in seen
                                and grid[next_row][next_col] == color
                            ):
                                seen.add(next_cell)
                                stack.append(next_cell)

                top = min(current_row for current_row, _ in component)
                bottom = max(current_row for current_row, _ in component)
                left = min(current_col for _, current_col in component)
                right = max(current_col for _, current_col in component)
                cells = set(component)
                patterns.append(
                    tuple(
                        tuple(
                            color if (current_row, current_col) in cells else 0
                            for current_col in range(left, right + 1)
                        )
                        for current_row in range(top, bottom + 1)
                    )
                )

    counts = Counter(patterns)
    selected = max(counts, key=counts.get)
    return [list(row) for row in selected]

from collections import Counter


def _largest_colored_component(grid, left, right, background):
    height = len(grid)
    seen = set()
    components = []

    for start_row in range(height):
        for start_col in range(left, right):
            if (
                grid[start_row][start_col] == background
                or (start_row, start_col) in seen
            ):
                continue

            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            component = []
            while stack:
                row, col = stack.pop()
                component.append((row, col - left, grid[row][col]))
                for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + drow
                    next_col = col + dcol
                    if (
                        0 <= next_row < height
                        and left <= next_col < right
                        and grid[next_row][next_col] != background
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            components.append(component)

    return max(components, key=len)


def transform(grid):
    """Combine each panel's largest colored fragment without overlaps."""
    height = len(grid)
    width = len(grid[0])
    background = Counter(
        value for row in grid for value in row if value != 0
    ).most_common(1)[0][0]

    separator_columns = {
        col
        for col in range(width)
        if all(grid[row][col] == 0 for row in range(height))
    }
    panels = []
    start = 0
    for col in range(width + 1):
        if col == width or col in separator_columns:
            if start < col:
                panels.append((start, col))
            start = col + 1

    output_width = max(right - left for left, right in panels)
    output = [
        [background for _ in range(output_width)]
        for _ in range(height)
    ]
    occupied = set()

    for left, right in panels:
        component = _largest_colored_component(grid, left, right, background)
        candidate_shifts = [0]
        for distance in range(1, output_width):
            candidate_shifts.extend((-distance, distance))

        shift = next(
            candidate
            for candidate in candidate_shifts
            if all(
                0 <= col + candidate < output_width
                and (row, col + candidate) not in occupied
                for row, col, _ in component
            )
        )
        for row, col, color in component:
            output[row][col + shift] = color
            occupied.add((row, col + shift))

    return output

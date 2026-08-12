

def transform(grid):
    """Combine each panel's largest colored fragment without overlaps."""
    height = len(grid)
    width = len(grid[0])
    background = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)

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
        _grid = grid
        _left = left
        _right = right
        _background = background
        height = len(_grid)
        seen = set()
        components = []

        for start_row in range(height):
            for start_col in range(_left, _right):
                if (
                    _grid[start_row][start_col] == _background
                    or (start_row, start_col) in seen
                ):
                    continue

                stack = [(start_row, start_col)]
                seen.add((start_row, start_col))
                component = []
                while stack:
                    row, col = stack.pop()
                    component.append((row, col - _left, _grid[row][col]))
                    for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + drow
                        next_col = col + dcol
                        if (
                            0 <= next_row < height
                            and _left <= next_col < _right
                            and _grid[next_row][next_col] != _background
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                components.append(component)

        _largest_colored_component_result_1 = max(components, key=len)
        component = _largest_colored_component_result_1
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

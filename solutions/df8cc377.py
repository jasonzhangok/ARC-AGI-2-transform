

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    frames = []
    frame_cells = set()

    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color == 0 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                cur_row, cur_col = stack.pop()
                component.append((cur_row, cur_col))
                for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = cur_row + d_row
                    next_col = cur_col + d_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and (next_row, next_col) not in seen
                            and grid[next_row][next_col] == color):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))

            top = min(r for r, _ in component)
            bottom = max(r for r, _ in component)
            left = min(c for _, c in component)
            right = max(c for _, c in component)
            border = {
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if r in (top, bottom) or c in (left, right)
            }
            if (bottom - top >= 2 and right - left >= 2
                    and set(component) == border):
                frames.append((color, top, bottom, left, right))
                frame_cells.update(border)

    loose_counts = {}
    for cell_value in (grid[row][col]
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0 and (row, col) not in frame_cells):
        loose_counts[cell_value] = loose_counts.get(cell_value, 0) + 1
    output = [[0] * width for _ in range(height)]
    for frame_color, top, bottom, left, right in frames:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if row in (top, bottom) or col in (left, right):
                    output[row][col] = frame_color
        interior_area = (bottom - top - 1) * (right - left - 1)
        needed = (interior_area + 1) // 2
        fill_color = next(
            color for color, count in loose_counts.items() if count == needed
        )
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                if ((row - top) + (col - left)) % 2 == 0:
                    output[row][col] = fill_color
    return output

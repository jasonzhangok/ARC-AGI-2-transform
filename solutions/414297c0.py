from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    canvas_color = Counter(
        value for row in grid for value in row if value != 0
    ).most_common(1)[0][0]

    canvas_cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == canvas_color
    ]
    top = min(row for row, _ in canvas_cells)
    bottom = max(row for row, _ in canvas_cells)
    left = min(col for _, col in canvas_cells)
    right = max(col for _, col in canvas_cells)

    target_by_color = {}
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            value = grid[row][col]
            if value not in (0, canvas_color):
                target_by_color.setdefault(value, []).append((row, col))

    output = [row[left : right + 1] for row in grid[top : bottom + 1]]
    seen = set()
    for start_row in range(height):
        for start_col in range(width):
            if (
                (start_row, start_col) in seen
                or grid[start_row][start_col] == 0
                or top <= start_row <= bottom
                and left <= start_col <= right
            ):
                continue

            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                component.append((row, col, grid[row][col]))
                for drow in (-1, 0, 1):
                    for dcol in (-1, 0, 1):
                        next_row, next_col = row + drow, col + dcol
                        if (
                            (drow != 0 or dcol != 0)
                            and 0 <= next_row < height
                            and 0 <= next_col < width
                            and (next_row, next_col) not in seen
                            and grid[next_row][next_col] != 0
                            and not (
                                top <= next_row <= bottom
                                and left <= next_col <= right
                            )
                        ):
                            seen.add((next_row, next_col))
                            queue.append((next_row, next_col))

            anchors = [cell for cell in component if cell[2] != 2]
            if len(anchors) != 1:
                continue
            anchor_row, anchor_col, anchor_color = anchors[0]
            targets = target_by_color.get(anchor_color, [])
            if len(targets) != 1:
                continue

            target_row, target_col = targets[0]
            for row, col, value in component:
                out_row = row + target_row - anchor_row - top
                out_col = col + target_col - anchor_col - left
                if 0 <= out_row < len(output) and 0 <= out_col < len(output[0]):
                    output[out_row][out_col] = value

    return output

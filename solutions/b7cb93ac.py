def _normalize(cells):
    min_row = min(row for row, _ in cells)
    min_col = min(col for _, col in cells)
    return frozenset((row - min_row, col - min_col) for row, col in cells)


def _variants(cells):
    """Return distinct rotations/reflections, preferring the original pose."""
    result = []
    current = set(cells)
    for _ in range(4):
        for pose in (current, {(row, -col) for row, col in current}):
            normalized = _normalize(pose)
            if normalized not in result:
                result.append(normalized)
        current = {(col, -row) for row, col in current}
    return result


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    pieces = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            color = grid[row][col]
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

            top_left = min(component)
            pieces.append((color, _normalize(component), top_left))

    pieces.sort(key=lambda item: (-len(item[1]), item[2]))
    canvas = [[0] * 4 for _ in range(3)]

    def place(piece_index):
        if piece_index == len(pieces):
            return all(value != 0 for line in canvas for value in line)

        color, cells, _ = pieces[piece_index]
        for pose in _variants(cells):
            pose_height = max(row for row, _ in pose) + 1
            pose_width = max(col for _, col in pose) + 1
            for top in range(4 - pose_height):
                for left in range(5 - pose_width):
                    target = [(top + row, left + col) for row, col in pose]
                    if all(canvas[row][col] == 0 for row, col in target):
                        for row, col in target:
                            canvas[row][col] = color
                        if place(piece_index + 1):
                            return True
                        for row, col in target:
                            canvas[row][col] = 0
        return False

    if not place(0):
        return []
    return canvas

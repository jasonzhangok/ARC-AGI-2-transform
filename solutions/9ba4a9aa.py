def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    order = []
    for row in grid:
        for color in row:
            if color not in counts:
                counts[color] = 0
                order.append(color)
            counts[color] += 1

    background = order[0]
    for color in order[1:]:
        if counts[color] > counts[background]:
            background = color
    guide_color = None
    for color in order:
        if color == background:
            continue
        if guide_color is None or counts[color] > counts[guide_color]:
            guide_color = color

    for row in range(height - 2):
        for col in range(width - 2):
            border = []
            for row_offset in range(3):
                for col_offset in range(3):
                    if row_offset in (0, 2) or col_offset in (0, 2):
                        border.append(grid[row + row_offset][col + col_offset])
            if (
                len(set(border)) != 1
                or border[0] == background
                or grid[row + 1][col + 1] == border[0]
            ):
                continue

            adjacent = []
            for offset in range(3):
                adjacent.append((row - 1, col + offset))
                adjacent.append((row + 3, col + offset))
                adjacent.append((row + offset, col - 1))
                adjacent.append((row + offset, col + 3))
            touches_guide = False
            for adjacent_row, adjacent_col in adjacent:
                if (
                    0 <= adjacent_row < height
                    and 0 <= adjacent_col < width
                    and grid[adjacent_row][adjacent_col] == guide_color
                ):
                    touches_guide = True
            if touches_guide:
                return [
                    grid[source_row][col:col + 3]
                    for source_row in range(row, row + 3)
                ]

    return []

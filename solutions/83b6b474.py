"""Arrange coloured components into a square frame."""


def transform(grid):
    """Pack the coloured components, without rotating them, into a square frame."""
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for colour in row:
            counts[colour] = counts.get(colour, 0) + 1
    background = max(counts, key=counts.get)

    seen = set()
    objects = []
    for row in range(height):
        for column in range(width):
            if (row, column) in seen or grid[row][column] == background:
                continue
            colour = grid[row][column]
            stack = [(row, column)]
            seen.add((row, column))
            cells = []
            while stack:
                current_row, current_column = stack.pop()
                cells.append((current_row, current_column))
                for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + delta_row
                    next_column = current_column + delta_column
                    if (
                        0 <= next_row < height
                        and 0 <= next_column < width
                        and (next_row, next_column) not in seen
                        and grid[next_row][next_column] == colour
                    ):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))
            top = min(cell[0] for cell in cells)
            left = min(cell[1] for cell in cells)
            objects.append(
                (colour, tuple(sorted((cell_row - top, cell_column - left) for cell_row, cell_column in cells)))
            )

    coloured_cell_count = sum(len(cells) for _, cells in objects)
    side = (coloured_cell_count + 4) // 4
    perimeter = {
        (row, column)
        for row in range(side)
        for column in range(side)
        if row in (0, side - 1) or column in (0, side - 1)
    }

    candidates = []
    for colour, cells in objects:
        placements = []
        for row_shift in range(side):
            for column_shift in range(side):
                placement = {(row + row_shift, column + column_shift) for row, column in cells}
                if placement <= perimeter:
                    placements.append((colour, placement))
        candidates.append(placements)

    def place(remaining, occupied, result):
        if not remaining:
            return result if occupied == perimeter else None
        object_index = min(
            remaining,
            key=lambda index: sum(not (cells & occupied) for _, cells in candidates[index]),
        )
        for colour, cells in candidates[object_index]:
            if not cells & occupied:
                arranged = place(
                    [index for index in remaining if index != object_index],
                    occupied | cells,
                    result + [(colour, cells)],
                )
                if arranged is not None:
                    return arranged
        return None

    arrangement = place(list(range(len(objects))), set(), [])
    if arrangement is None:
        raise ValueError("The components cannot form a complete square perimeter")

    output = [[background for _ in range(side)] for _ in range(side)]
    for colour, cells in arrangement:
        for row, column in cells:
            output[row][column] = colour
    return output

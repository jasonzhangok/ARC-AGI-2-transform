def transform(grid: list[list[int]]) -> list[list[int]]:
    """Return the colored rectangle outlines from bottom layer to top layer."""
    background = 8
    colors = sorted({value for row in grid for value in row if value != background})
    bounds: dict[int, tuple[int, int, int, int]] = {}

    for color in colors:
        cells = [
            (row_index, column_index)
            for row_index, row in enumerate(grid)
            for column_index, value in enumerate(row)
            if value == color
        ]
        bounds[color] = (
            min(row for row, _ in cells),
            max(row for row, _ in cells),
            min(column for _, column in cells),
            max(column for _, column in cells),
        )

    def is_on_outline(color: int, row: int, column: int) -> bool:
        top, bottom, left, right = bounds[color]
        return (
            top <= row <= bottom
            and left <= column <= right
            and (row == top or row == bottom or column == left or column == right)
        )

    above: dict[int, set[int]] = {color: set() for color in colors}
    for row_index, row in enumerate(grid):
        for column_index, visible_color in enumerate(row):
            outlines_here = [
                color
                for color in colors
                if is_on_outline(color, row_index, column_index)
            ]
            if len(outlines_here) > 1 and visible_color in outlines_here:
                for covered_color in outlines_here:
                    if covered_color != visible_color:
                        above[covered_color].add(visible_color)

    incoming = {color: 0 for color in colors}
    for covered_colors in above.values():
        for color in covered_colors:
            incoming[color] += 1

    order: list[int] = []
    available = [color for color in colors if incoming[color] == 0]
    while available:
        color = min(available, key=lambda item: (*bounds[item], item))
        available.remove(color)
        order.append(color)
        for upper_color in above[color]:
            incoming[upper_color] -= 1
            if incoming[upper_color] == 0:
                available.append(upper_color)

    return [[color] for color in order]

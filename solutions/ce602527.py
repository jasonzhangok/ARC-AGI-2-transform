"""Extract the object whose doubled pattern appears as a clipped larger copy."""

from collections import Counter


def _bounding_box(grid, color):
    points = [
        (row, column)
        for row, values in enumerate(grid)
        for column, value in enumerate(values)
        if value == color
    ]
    top = min(row for row, _ in points)
    bottom = max(row for row, _ in points)
    left = min(column for _, column in points)
    right = max(column for _, column in points)
    return top, bottom, left, right


def _color_mask(grid, color, box):
    top, bottom, left, right = box
    return [
        [int(grid[row][column] == color) for column in range(left, right + 1)]
        for row in range(top, bottom + 1)
    ]


def _double(mask):
    doubled = []
    for row in mask:
        doubled_row = [value for value in row for _ in range(2)]
        doubled.extend([doubled_row[:], doubled_row[:]])
    return doubled


def _contains(whole, part):
    whole_height, whole_width = len(whole), len(whole[0])
    part_height, part_width = len(part), len(part[0])
    if part_height > whole_height or part_width > whole_width:
        return False

    return any(
        all(
            part[row][column] == whole[top + row][left + column]
            for row in range(part_height)
            for column in range(part_width)
        )
        for top in range(whole_height - part_height + 1)
        for left in range(whole_width - part_width + 1)
    )


def transform(grid):
    """Return the source pattern of a larger, possibly boundary-clipped 2x copy."""
    height = len(grid)
    width = len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = max(counts, key=counts.get)
    colors = [color for color in counts if color != background]

    boxes = {color: _bounding_box(grid, color) for color in colors}
    masks = {
        color: _color_mask(grid, color, boxes[color])
        for color in colors
    }

    sources = []
    for source in colors:
        doubled = _double(masks[source])
        for larger_copy in colors:
            if larger_copy == source or counts[larger_copy] <= counts[source]:
                continue
            top, bottom, left, right = boxes[larger_copy]
            if not (
                top == 0
                or bottom == height - 1
                or left == 0
                or right == width - 1
            ):
                continue
            if _contains(doubled, masks[larger_copy]):
                sources.append(source)
                break

    if len(sources) != 1:
        raise ValueError("expected exactly one object with a clipped doubled copy")

    top, bottom, left, right = boxes[sources[0]]
    return [row[left : right + 1] for row in grid[top : bottom + 1]]

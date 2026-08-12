from collections import deque


def _components(grid, value_test):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if value_test(grid[r][c])}
    result = []
    while remaining:
        start = remaining.pop()
        queue = deque([start])
        component = {start}
        while queue:
            row, col = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                point = (row + dr, col + dc)
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        result.append(component)
    return result


def _shape(component):
    top = min(r for r, _ in component)
    left = min(c for _, c in component)
    return frozenset((r - top, c - left) for r, c in component)


def _can_tile(hole, piece, copies):
    piece_shape = _shape(piece)
    placements = []
    for anchor in hole:
        min_row = min(r for r, _ in piece_shape)
        min_col = min(c for _, c in piece_shape)
        shifted = {(anchor[0] + r - min_row, anchor[1] + c - min_col) for r, c in piece_shape}
        if shifted <= hole and shifted not in placements:
            placements.append(shifted)

    def search(uncovered, remaining):
        if not uncovered:
            return remaining == 0
        if remaining == 0:
            return False
        point = next(iter(uncovered))
        return any(
            search(uncovered - placement, remaining - 1)
            for placement in placements
            if point in placement and placement <= uncovered
        )

    return len(hole) == len(piece) * copies and search(set(hole), copies)


def transform(grid):
    height, width = len(grid), len(grid[0])
    zero_components = _components(grid, lambda value: value == 0)
    holes = [
        component
        for component in zero_components
        if not any(r in (0, height - 1) or c in (0, width - 1) for r, c in component)
    ]
    colors = {value for row in grid for value in row if value not in (0, 5)}
    colored = []
    for color in colors:
        colored.extend(_components(grid, lambda value, target=color: value == target))
    main = set()
    for component in colored:
        if any(
            (r + dr, c + dc) in hole
            for r, c in component
            for hole in holes
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
        ):
            main |= component
    small = [component for component in colored if component.isdisjoint(main)]

    output = [[0] * width for _ in range(height)]
    for row, col in main:
        output[row][col] = grid[row][col]
    hole_cells = set().union(*holes)
    pieces = []
    for component in small:
        point = next(iter(component))
        shape = _shape(component)
        color = grid[point[0]][point[1]]
        placements = []
        for anchor in hole_cells:
            shifted = {(anchor[0] + r, anchor[1] + c) for r, c in shape}
            if shifted <= hole_cells and shifted not in placements:
                placements.append(shifted)
        pieces.append((color, placements))

    def cover(uncovered, unused, coloring):
        if not uncovered:
            return coloring
        point = next(iter(uncovered))
        for index in unused:
            color, placements = pieces[index]
            for placement in placements:
                if point in placement and placement <= uncovered:
                    result = cover(
                        uncovered - placement,
                        unused - {index},
                        coloring + [(color, placement)],
                    )
                    if result is not None:
                        return result
        return None

    coloring = cover(hole_cells, set(range(len(pieces))), [])
    if coloring is not None:
        for color, placement in coloring:
            for row, col in placement:
                output[row][col] = color
    return output

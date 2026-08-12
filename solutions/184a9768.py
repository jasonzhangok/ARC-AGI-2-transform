def transform(grid):
    height, width = len(grid), len(grid[0])
    zero_remaining = {(r, c) for r in range(height) for c in range(width)
                      if grid[r][c] == 0}
    zero_components = []
    while zero_remaining:
        start = zero_remaining.pop()
        queue = [start]
        component = {start}
        position = 0
        while position < len(queue):
            row, col = queue[position]
            position += 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                point = row + dr, col + dc
                if point in zero_remaining:
                    zero_remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        zero_components.append(component)
    holes = [component for component in zero_components
             if not any(r in (0, height - 1) or c in (0, width - 1)
                        for r, c in component)]

    colors = {value for row in grid for value in row if value not in (0, 5)}
    colored = []
    for color in colors:
        remaining = {(r, c) for r in range(height) for c in range(width)
                     if grid[r][c] == color}
        while remaining:
            start = remaining.pop()
            queue = [start]
            component = {start}
            position = 0
            while position < len(queue):
                row, col = queue[position]
                position += 1
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    point = row + dr, col + dc
                    if point in remaining:
                        remaining.remove(point)
                        component.add(point)
                        queue.append(point)
            colored.append(component)

    main = set()
    for component in colored:
        if any((r + dr, c + dc) in hole
               for r, c in component for hole in holes
               for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))):
            main |= component
    small = [component for component in colored if component.isdisjoint(main)]
    output = [[0] * width for _ in range(height)]
    for row, col in main:
        output[row][col] = grid[row][col]
    hole_cells = set().union(*holes)
    pieces = []
    for component in small:
        point = next(iter(component))
        top = min(r for r, _ in component)
        left = min(c for _, c in component)
        shape = frozenset((r - top, c - left) for r, c in component)
        color = grid[point[0]][point[1]]
        placements = []
        for anchor in hole_cells:
            shifted = {(anchor[0] + r, anchor[1] + c) for r, c in shape}
            if shifted <= hole_cells and shifted not in placements:
                placements.append(shifted)
        pieces.append((color, placements))

    coloring = None
    stack = [(hole_cells, set(range(len(pieces))), [])]
    while stack and coloring is None:
        uncovered, unused, partial = stack.pop()
        if not uncovered:
            coloring = partial
            break
        point = next(iter(uncovered))
        options = []
        for index in unused:
            color, placements = pieces[index]
            for placement in placements:
                if point in placement and placement <= uncovered:
                    options.append((index, color, placement))
        for index, color, placement in reversed(options):
            stack.append((uncovered - placement, unused - {index},
                          partial + [(color, placement)]))
    if coloring is not None:
        for color, placement in coloring:
            for row, col in placement:
                output[row][col] = color
    return output

def transform(grid):
    points = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0}
    components = []
    while points:
        start = points.pop()
        stack = [start]
        component = {start}
        while stack:
            row, col = stack.pop()
            neighbors = {
                (r, c)
                for r, c in points
                if abs(r - row) <= 2 and abs(c - col) <= 2
            }
            points -= neighbors
            component |= neighbors
            stack.extend(neighbors)
        components.append(component)
    components.sort(key=lambda comp: (min(r for r, _ in comp), min(c for _, c in comp)))
    top_two = sorted(components[:2], key=lambda comp: min(c for _, c in comp))
    bottom_two = sorted(components[2:], key=lambda comp: min(c for _, c in comp))
    ordered = top_two + bottom_two
    output = [[0] * 7 for _ in range(7)]
    for index, component in enumerate(ordered):
        top = min(r for r, _ in component)
        left = min(c for _, c in component)
        target_row = 0 if index < 2 else 4
        target_col = 0 if index % 2 == 0 else 4
        for row, col in component:
            output[target_row + row - top][target_col + col - left] = grid[row][col]
    return output

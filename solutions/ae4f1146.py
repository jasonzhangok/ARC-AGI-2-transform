def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = {(row, col) for row in range(height) for col in range(width) if grid[row][col] != 0}
    components = []
    while remaining:
        pending = [remaining.pop()]
        component = set(pending)
        while pending:
            row, col = pending.pop()
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        components.append(component)
    chosen = max(((sum((grid[row][col] == 1 for row, col in _key_item_1)), -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(components)))[2]
    top = min((row for row, _ in chosen))
    bottom = max((row for row, _ in chosen))
    left = min((col for _, col in chosen))
    right = max((col for _, col in chosen))
    output = [grid[row][left:right + 1] for row in range(top, bottom + 1)]
    return output

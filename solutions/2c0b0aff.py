from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, column)
        for row in range(height)
        for column in range(width)
        if grid[row][column] != 0
    }
    components = []

    while remaining:
        start = remaining.pop()
        component = {start}
        queue = deque([start])
        while queue:
            row, column = queue.popleft()
            for neighbor in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        components.append(component)

    def cross_count(component):
        return sum(
            grid[row][column] == 3
            and all(
                (neighbor_row, neighbor_column) in component
                and grid[neighbor_row][neighbor_column] == 3
                for neighbor_row, neighbor_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                )
            )
            for row, column in component
        )

    selected = max(components, key=cross_count)
    top = min(row for row, _ in selected)
    bottom = max(row for row, _ in selected)
    left = min(column for _, column in selected)
    right = max(column for _, column in selected)
    return [grid[row][left:right + 1] for row in range(top, bottom + 1)]

def transform(grid):
    """Rotate each isolated foreground line 90 degrees about its center."""
    height = len(grid)
    if height == 0:
        output = []
    else:
        width = len(grid[0])
        counts = {}
        for row in grid:
            for color in row:
                counts[color] = counts.get(color, 0) + 1
        background = max(counts, key=counts.get)
        result = [[background for _ in range(width)] for _ in range(height)]
        unseen = {(row, col) for row in range(height) for col in range(width) if grid[row][col] != background}
        while unseen:
            start = unseen.pop()
            component = [start]
            stack = [start]
            while stack:
                row, col = stack.pop()
                for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        component.append(neighbor)
                        stack.append(neighbor)
            rows = [row for row, _ in component]
            cols = [col for _, col in component]
            center_row = (min(rows) + max(rows)) // 2
            center_col = (min(cols) + max(cols)) // 2
            for row, col in component:
                new_row = center_row + (col - center_col)
                new_col = center_col - (row - center_row)
                if 0 <= new_row < height and 0 <= new_col < width:
                    result[new_row][new_col] = grid[row][col]
        output = result
    return output

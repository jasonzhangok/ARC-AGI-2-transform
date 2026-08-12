def transform(grid):
    result = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0]) if height else 0
    seen = [[False] * width for _ in range(height)]
    blocks = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2 or seen[row][col]:
                continue
            component = []
            stack = [(row, col)]
            seen[row][col] = True
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for next_row, next_col in ((current_row - 1, current_col), (current_row + 1, current_col), (current_row, current_col - 1), (current_row, current_col + 1)):
                    if 0 <= next_row < height and 0 <= next_col < width and not seen[next_row][next_col] and grid[next_row][next_col] == 2:
                        seen[next_row][next_col] = True
                        stack.append((next_row, next_col))
            rows = [cell[0] for cell in component]
            cols = [cell[1] for cell in component]
            if len(component) == 4 and max(rows) - min(rows) == 1 and max(cols) - min(cols) == 1:
                blocks.append((min(cols), component))

    blocks.sort(reverse=True)
    for index, block_entry in enumerate(blocks):
        if index % 2 == 0:
            block = block_entry[1]
            for row, col in block:
                result[row][col] = 8
    output = result
    return output

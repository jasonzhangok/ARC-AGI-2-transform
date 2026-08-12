def transform(grid):
    height, width = (len(grid), len(grid[0]))
    result = [row[:] for row in grid]
    source = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 3]
    target = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2]
    horizontal = len({r for r, _ in source}) == 1
    if horizontal:
        source_row = source[0][0]
        target_row = target[0][0]
        source_center = sum((c for _, c in source)) / len(source)
        target_center = sum((c for _, c in target)) / len(target)
        if source_center != target_center:
            direction = 1 if target_center > source_center else -1
        else:
            direction = 1 if source_center < width / 2 else -1
        front = (max if direction > 0 else min)((c for _, c in source))
        junction = front + direction
        while 0 <= junction < width and grid[source_row][junction] != 8:
            junction += direction
        junction -= direction
        for c in range(min(front + direction, junction), max(front + direction, junction) + 1):
            if grid[source_row][c] == 0:
                result[source_row][c] = 3
        nearest_target_column = min(((abs(_key_item_1 - junction), _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate((c for _, c in target))))[2]
        for c in range(min(nearest_target_column, junction), max(nearest_target_column, junction) + 1):
            if grid[target_row][c] == 0:
                result[target_row][c] = 3
        for r in range(min(source_row, target_row), max(source_row, target_row) + 1):
            if grid[r][junction] == 0:
                result[r][junction] = 3
    else:
        source_column = source[0][1]
        target_column = target[0][1]
        source_center = sum((r for r, _ in source)) / len(source)
        target_center = sum((r for r, _ in target)) / len(target)
        if source_center != target_center:
            direction = 1 if target_center > source_center else -1
        else:
            direction = 1 if source_center < height / 2 else -1
        front = (max if direction > 0 else min)((r for r, _ in source))
        junction = front + direction
        while 0 <= junction < height and grid[junction][source_column] != 8:
            junction += direction
        junction -= direction
        for r in range(min(front + direction, junction), max(front + direction, junction) + 1):
            if grid[r][source_column] == 0:
                result[r][source_column] = 3
        nearest_target_row = min(((abs(_key_item_2 - junction), _key_index_2, _key_item_2) for _key_index_2, _key_item_2 in enumerate((r for r, _ in target))))[2]
        for r in range(min(nearest_target_row, junction), max(nearest_target_row, junction) + 1):
            if grid[r][target_column] == 0:
                result[r][target_column] = 3
        for c in range(min(source_column, target_column), max(source_column, target_column) + 1):
            if grid[junction][c] == 0:
                result[junction][c] = 3
    output = result
    return output

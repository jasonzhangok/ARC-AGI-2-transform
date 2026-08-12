def transform(grid):
    height, width = len(grid), len(grid[0])
    objects = []
    row = 0

    while row < height:
        colors = {value for value in grid[row] if value != 0}
        if not colors:
            row += 1
            continue

        color = next(iter(colors))
        first_row = row
        while row + 1 < height:
            next_colors = {value for value in grid[row + 1] if value != 0}
            if next_colors != {color}:
                break
            row += 1
        objects.append((first_row, [line[:] for line in grid[first_row:row + 1]]))
        row += 1

    output = [[0] * width for _ in range(height)]
    destination_row = objects[0][0]
    for _, object_rows in reversed(objects):
        for object_row in object_rows:
            output[destination_row] = object_row[:]
            destination_row += 1

    return output

def transform(grid):
    height = len(grid)
    width = len(grid[0])

    groups = []
    col = 0
    while col < width:
        if grid[0][col] != 0:
            start = col
            while col + 1 < width and grid[0][col + 1] != 0:
                col += 1
            groups.append((start, col))
        col += 1

    counts = []
    for start, end in groups:
        count = 0
        for row in range(height):
            for col in range(start, end + 1):
                if grid[row][col] != 0:
                    count += 1
        counts.append(count)

    order = []
    for group in range(len(groups)):
        position = len(order)
        while position > 0 and counts[group] < counts[order[position - 1]]:
            position -= 1
        order.insert(position, group)

    output = [row[:] for row in grid]
    for destination, source in enumerate(order):
        destination_start, destination_end = groups[destination]
        source_start, source_end = groups[source]
        for row in range(height):
            for offset in range(destination_end - destination_start + 1):
                output[row][destination_start + offset] = grid[row][source_start + offset]
    return output

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    endpoints = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    ]

    distance_maps = []
    for start in endpoints:
        result = {start: 0}
        queue = [start]
        position = 0
        while position < len(queue):
            row, col = queue[position]
            position += 1
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                nr, nc = neighbor
                if (
                    0 <= nr < height
                    and 0 <= nc < width
                    and grid[nr][nc] != 1
                    and neighbor not in result
                ):
                    result[neighbor] = result[row, col] + 1
                    queue.append(neighbor)
        distance_maps.append(result)
    from_first, from_second = distance_maps
    shortest = from_first[endpoints[1]]
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            cell = (row, col)
            if (
                grid[row][col] == 0
                and cell in from_first
                and cell in from_second
                and from_first[cell] + from_second[cell] == shortest
            ):
                output[row][col] = 4
    return output

def transform(grid):
    height, width = len(grid), len(grid[0])
    region_at = {}
    regions = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 7 or (row, col) in region_at:
                continue
            region_index = len(regions)
            queue = [(row, col)]
            region_at[(row, col)] = region_index
            region = []
            for current_row, current_col in queue:
                region.append((current_row, current_col))
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = current_row + row_step, current_col + col_step
                    if (0 <= neighbor[0] < height and 0 <= neighbor[1] < width
                            and grid[neighbor[0]][neighbor[1]] == 7
                            and neighbor not in region_at):
                        region_at[neighbor] = region_index
                        queue.append(neighbor)
            regions.append(region)

    adjacency = [set() for _ in regions]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2:
                continue
            neighbors = {
                region_at[neighbor]
                for neighbor in ((row - 1, col), (row + 1, col),
                                 (row, col - 1), (row, col + 1))
                if neighbor in region_at
            }
            for first in neighbors:
                adjacency[first].update(neighbors - {first})

    outer = max(
        range(len(regions)),
        key=lambda index: sum(
            row in (0, height - 1) or col in (0, width - 1)
            for row, col in regions[index]
        ),
    )
    distance = {outer: 0}
    queue = [outer]
    for region in queue:
        for neighbor in adjacency[region]:
            if neighbor not in distance:
                distance[neighbor] = distance[region] + 1
                queue.append(neighbor)
    deepest = max(distance.values())

    output = [row[:] for row in grid]
    for index, region in enumerate(regions):
        color = 5 if (deepest - distance[index]) % 2 == 0 else 3
        for row, col in region:
            output[row][col] = color
    return output

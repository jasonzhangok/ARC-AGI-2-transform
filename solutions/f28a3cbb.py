def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    output = [[background for _ in range(width)] for _ in range(height)]
    colors = {value for value in counts if value != background}

    for color in colors:
        all_points = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        unseen = set(all_points)
        components = []
        while unseen:
            start = unseen.pop()
            component = {start}
            frontier = [start]
            while frontier:
                row, col = frontier.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + dr, col + dc)
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        component.add(neighbor)
                        frontier.append(neighbor)
            components.append(component)

        main = components[0]
        for component in components[1:]:
            if len(component) > len(main):
                main = component
        top = min(row for row, col in main)
        bottom = max(row for row, col in main)
        left = min(col for row, col in main)
        right = max(col for row, col in main)
        for row, col in main:
            output[row][col] = color

        for row, col in all_points - main:
            nearest_row = min(max(row, top), bottom)
            nearest_col = min(max(col, left), right)
            row_distance = row - nearest_row
            col_distance = col - nearest_col
            if abs(col_distance) > abs(row_distance):
                projected_col = left - 1 if col_distance < 0 else right + 1
                if 0 <= projected_col < width:
                    output[nearest_row][projected_col] = color
            elif abs(row_distance) > abs(col_distance):
                projected_row = top - 1 if row_distance < 0 else bottom + 1
                if 0 <= projected_row < height:
                    output[projected_row][nearest_col] = color
    return output

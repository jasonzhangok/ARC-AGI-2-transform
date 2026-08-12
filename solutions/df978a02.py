def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = 8
    groups = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color != background:
                if color not in groups:
                    groups[color] = []
                groups[color].append((row, col))
    output = [row[:] for row in grid]
    colors = list(groups)
    if not colors:
        output = output
    else:
        winner = colors[0]
        for color in colors[1:]:
            if len(groups[color]) > len(groups[winner]):
                winner = color
        center_row = (height - 1) / 2
        center_col = (width - 1) / 2
        for color in colors:
            points = groups[color]
            tip_row, tip_col = points[0]
            tip_distance = abs(tip_row - center_row) + abs(tip_col - center_col)
            for row, col in points[1:]:
                distance = abs(row - center_row) + abs(col - center_col)
                if distance < tip_distance:
                    tip_row, tip_col = (row, col)
                    tip_distance = distance
            if color != winner:
                output[tip_row][tip_col] = background
            else:
                average_row = sum((point[0] for point in points)) / len(points)
                average_col = sum((point[1] for point in points)) / len(points)
                if abs(average_row - center_row) >= abs(average_col - center_col):
                    if average_row < center_row:
                        cap_row = min((point[0] for point in points)) - 1
                    else:
                        cap_row = max((point[0] for point in points)) + 1
                    if 0 <= cap_row < height:
                        for cap_col in range(tip_col - 1, tip_col + 2):
                            if 0 <= cap_col < width:
                                output[cap_row][cap_col] = color
                else:
                    if average_col < center_col:
                        cap_col = min((point[1] for point in points)) - 1
                    else:
                        cap_col = max((point[1] for point in points)) + 1
                    if 0 <= cap_col < width:
                        for cap_row in range(tip_row - 1, tip_row + 2):
                            if 0 <= cap_row < height:
                                output[cap_row][cap_col] = color
        output = output
    return output

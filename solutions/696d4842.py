def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    colors = {value for row in grid for value in row if value != 0}
    groups = {}
    for color in colors:
        groups[color] = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }

    paths = []
    markers = []
    for color, points in groups.items():
        if len(points) == 1:
            markers.append((color, next(iter(points))))
        else:
            paths.append((color, points))

    for color, points in paths:
        endpoints = []
        for row, col in points:
            degree = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (row + dr, col + dc) in points:
                    degree += 1
            if degree == 1:
                endpoints.append((row, col))

        matched_index = None
        matched_marker_color = None
        matched_marker = None
        for index, endpoint in enumerate(endpoints):
            inward = None
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (endpoint[0] + dr, endpoint[1] + dc)
                if neighbor in points:
                    inward = (dr, dc)
                    break
            for marker_color, marker in markers:
                marker_dr = marker[0] - endpoint[0]
                marker_dc = marker[1] - endpoint[1]
                aligned = marker_dr == 0 or marker_dc == 0
                outward = marker_dr * inward[0] + marker_dc * inward[1] < 0
                if aligned and outward:
                    matched_index = index
                    matched_marker_color = marker_color
                    matched_marker = marker
                    break
            if matched_index is not None:
                break

        near_endpoint = endpoints[matched_index]
        far_endpoint = endpoints[1 - matched_index]
        gap_length = (
            abs(near_endpoint[0] - matched_marker[0]) +
            abs(near_endpoint[1] - matched_marker[1]) - 1
        )
        if near_endpoint[0] == matched_marker[0]:
            dr = 0
        elif matched_marker[0] > near_endpoint[0]:
            dr = 1
        else:
            dr = -1
        if near_endpoint[1] == matched_marker[1]:
            dc = 0
        elif matched_marker[1] > near_endpoint[1]:
            dc = 1
        else:
            dc = -1

        row, col = near_endpoint
        for _ in range(gap_length):
            row += dr
            col += dc
            output[row][col] = color

        previous = None
        current = far_endpoint
        for _ in range(gap_length):
            output[current[0]][current[1]] = matched_marker_color
            next_point = None
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (current[0] + dr, current[1] + dc)
                if neighbor in points and neighbor != previous:
                    next_point = neighbor
                    break
            previous = current
            current = next_point
    return output

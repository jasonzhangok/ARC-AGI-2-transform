def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    output = [row[:] for row in grid]

    colors = {value for row in grid for value in row if value != background}
    for color in colors:
        remaining = {(r, c) for r in range(height) for c in range(width)
                     if grid[r][c] == color}
        components = []
        while remaining:
            first = remaining.pop()
            component = {first}
            frontier = [first]
            while frontier:
                r, c = frontier.pop()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (r + dr, c + dc)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        frontier.append(neighbor)
            components.append(component)

        body = max(components, key=len)
        top = min(r for r, c in body)
        bottom = max(r for r, c in body)
        left = min(c for r, c in body)
        right = max(c for r, c in body)

        markers = set()
        for component in components:
            if component is not body:
                markers.update(component)

        for marker_r, marker_c in markers:
            if marker_c < left:
                step_r, step_c = 0, -1
                start_r, start_c = marker_r, left - 1
            elif marker_c > right:
                step_r, step_c = 0, 1
                start_r, start_c = marker_r, right + 1
            elif marker_r < top:
                step_r, step_c = -1, 0
                start_r, start_c = top - 1, marker_c
            else:
                step_r, step_c = 1, 0
                start_r, start_c = bottom + 1, marker_c

            r, c = start_r, start_c
            while (r, c) != (marker_r, marker_c):
                output[r][c] = color
                r += step_r
                c += step_c

            if step_r == 0:
                for r in (start_r - 1, start_r + 1):
                    if 0 <= r < height:
                        output[r][start_c] = color
            else:
                for c in (start_c - 1, start_c + 1):
                    if 0 <= c < width:
                        output[start_r][c] = color

            output[marker_r][marker_c] = background
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r, c = marker_r + dr, marker_c + dc
                if 0 <= r < height and 0 <= c < width:
                    output[r][c] = color

    return output

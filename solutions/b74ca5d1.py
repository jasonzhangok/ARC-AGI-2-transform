from collections import Counter


def _object_box(grid, row, col, background, key_colors):
    """Find the unique 5-by-5 two-color object containing a key pixel."""
    height, width = len(grid), len(grid[0])
    candidates = []

    for top in range(max(0, row - 4), min(row, height - 5) + 1):
        for left in range(max(0, col - 4), min(col, width - 5) + 1):
            cells = [
                grid[r][c]
                for r in range(top, top + 5)
                for c in range(left, left + 5)
                if grid[r][c] != background
            ]
            if set(cells) != {grid[row][col]} | (
                set(cells) - key_colors
            ):
                continue
            if len(set(cells)) != 2:
                continue
            if sum(color in key_colors for color in cells) != 1:
                continue

            touches_every_side = (
                any(grid[top][c] != background for c in range(left, left + 5))
                and any(
                    grid[top + 4][c] != background
                    for c in range(left, left + 5)
                )
                and any(grid[r][left] != background for r in range(top, top + 5))
                and any(
                    grid[r][left + 4] != background
                    for r in range(top, top + 5)
                )
            )
            if touches_every_side:
                candidates.append((top, left))

    if len(candidates) != 1:
        return None
    return candidates[0]


def _four_components(points):
    remaining = set(points)
    components = []
    while remaining:
        stack = [remaining.pop()]
        component = set(stack)
        while stack:
            row, col = stack.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    stack.append(neighbor)
                    component.add(neighbor)
        components.append(component)
    return components


def transform(grid):
    output = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]

    corners = ((0, 0), (0, width - 1), (height - 1, 0), (height - 1, width - 1))
    corner_set = set(corners)
    key_to_corners = {}
    for row, col in corners:
        color = grid[row][col]
        if color != background:
            key_to_corners.setdefault(color, []).append((row, col))

    key_colors = set(key_to_corners)
    objects = {color: [] for color in key_colors}

    for row in range(height):
        for col in range(width):
            key = grid[row][col]
            if (row, col) in corner_set or key not in key_colors:
                continue

            box = _object_box(grid, row, col, background, key_colors)
            if box is None:
                continue
            top, left = box
            body_colors = {
                grid[r][c]
                for r in range(top, top + 5)
                for c in range(left, left + 5)
                if grid[r][c] not in (background, key)
            }
            if len(body_colors) != 1:
                continue
            body = body_colors.pop()
            mask = {
                (r - top, c - left)
                for r in range(top, top + 5)
                for c in range(left, left + 5)
                if grid[r][c] != background
            }
            marker = (row - top, col - left)
            components = _four_components(mask - {marker})
            largest = max(len(component) for component in components)
            adjacent_to_largest = any(
                abs(r - marker[0]) + abs(c - marker[1]) == 1
                for component in components
                if len(component) == largest
                for r, c in component
            )
            corner_mask = set(mask)
            if len(components) == 2 and len(components[0]) != len(components[1]):
                corner_mask = {
                    point
                    for component in components
                    if len(component) == largest
                    for point in component
                } | {marker}
            objects[key].append(
                {
                    "top": top,
                    "left": left,
                    "body": body,
                    "marker": marker,
                    "mask": mask,
                    "corner_mask": corner_mask,
                    "adjacent_to_largest": adjacent_to_largest,
                }
            )

    for key, group in objects.items():
        for index, obj in enumerate(group):
            top, left, body = obj["top"], obj["left"], obj["body"]
            marker = obj["marker"]
            marker_replacement = body
            if index and (0 in marker or 4 in marker) and not obj["adjacent_to_largest"]:
                for earlier in group[:index]:
                    if marker in earlier["mask"] and marker != earlier["marker"]:
                        marker_replacement = earlier["body"]
                        break
            for r in range(top, top + 5):
                for c in range(left, left + 5):
                    if grid[r][c] == body:
                        output[r][c] = key
                    elif grid[r][c] == key:
                        output[r][c] = marker_replacement

    for key, destinations in key_to_corners.items():
        if not objects[key]:
            continue
        mask = set().union(*(obj["corner_mask"] for obj in objects[key]))
        for corner_row, corner_col in destinations:
            top = 0 if corner_row == 0 else height - 5
            left = 0 if corner_col == 0 else width - 5
            for r in range(top, top + 5):
                for c in range(left, left + 5):
                    output[r][c] = background
            for dr, dc in mask:
                output[top + dr][left + dc] = key

    return output

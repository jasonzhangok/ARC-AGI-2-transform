def transform(grid):
    height = len(grid)
    width = len(grid[0])
    markers = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 3:
                markers.append((row, column))
    marker_set = set(markers)
    marker_indices = {}
    for index, marker in enumerate(markers):
        marker_indices[marker] = index

    candidates_by_mask = {}
    for apex_row in range(height):
        for apex_column in range(width):
            for depth in range(2, max(height, width) + 1):
                for row_direction, column_direction in ((1, 0), (-1, 0),
                                                         (0, 1), (0, -1)):
                    shape = set()
                    boundary = set()
                    for distance in range(depth + 1):
                        center_row = apex_row + row_direction * distance
                        center_column = apex_column + column_direction * distance
                        for side_offset in range(-distance, distance + 1):
                            row = center_row - column_direction * side_offset
                            column = center_column + row_direction * side_offset
                            if 0 <= row < height and 0 <= column < width:
                                shape.add((row, column))
                                if abs(side_offset) == distance or distance == depth:
                                    boundary.add((row, column))
                    boundary_markers = marker_set & boundary
                    if len(boundary_markers) < 3 or (marker_set - boundary_markers) & shape:
                        continue
                    mask = 0
                    for marker in boundary_markers:
                        mask |= 1 << marker_indices[marker]
                    candidate = (len(shape), depth, shape)
                    if (mask not in candidates_by_mask
                            or candidate[:2] < candidates_by_mask[mask][:2]):
                        candidates_by_mask[mask] = candidate

    candidates = []
    for mask, candidate in candidates_by_mask.items():
        candidates.append((mask, candidate[0], candidate[1], candidate[2]))

    full_mask = (1 << len(markers)) - 1
    covers = {0: (0, 0, [])}
    for covered_mask in range(full_mask + 1):
        if covered_mask not in covers:
            continue
        for candidate_index, candidate in enumerate(candidates):
            marker_mask, area, _, _ = candidate
            if marker_mask & covered_mask:
                continue
            new_mask = covered_mask | marker_mask
            new_cover = (covers[covered_mask][0] + 1,
                         covers[covered_mask][1] + area,
                         covers[covered_mask][2] + [candidate_index])
            if (new_mask not in covers
                    or new_cover[:2] < covers[new_mask][:2]):
                covers[new_mask] = new_cover

    output = [row[:] for row in grid]
    if full_mask in covers:
        for candidate_index in covers[full_mask][2]:
            for row, column in candidates[candidate_index][3]:
                if output[row][column] != 3:
                    output[row][column] = 8
    return output

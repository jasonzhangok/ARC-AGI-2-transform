def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts={}
    for source_row in grid:
        for value in source_row:counts[value]=counts.get(value,0)+1
    background=None
    for value in counts:
        if background is None or counts[value]>counts[background]:background=value
    output = [row[:] for row in grid]

    for color, radius_change in ((2, -1), (5, 1)):
        cells = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        for row, col in cells:
            output[row][col] = background

        remaining=set(cells);components=[]
        while remaining:
            start=remaining.pop();stack=[start];component={start}
            while stack:
                component_row,component_col=stack.pop()
                for dr in (-1,0,1):
                    for dc in (-1,0,1):
                        neighbor=(component_row+dr,component_col+dc)
                        if neighbor in remaining:remaining.remove(neighbor);component.add(neighbor);stack.append(neighbor)
            components.append(component)
        for component in components:
            sample_row,sample_col=next(iter(component));candidates=[]
            for candidate_center_row in range(-height,2*height):
                for candidate_center_col in range(-width,2*width):
                    candidate_radius=abs(sample_row-candidate_center_row)+abs(sample_col-candidate_center_col)
                    visible={(ring_row,ring_col) for ring_row in range(height) for ring_col in range(width) if abs(ring_row-candidate_center_row)+abs(ring_col-candidate_center_col)==candidate_radius}
                    if visible==component:candidates.append((candidate_radius,candidate_center_row,candidate_center_col))
            ring=None if not candidates else (min(candidates)[1],min(candidates)[2],min(candidates)[0])
            if ring is None:
                for row, col in component:
                    output[row][col] = color
                continue

            center_row, center_col, radius = ring
            new_radius = radius + radius_change
            if new_radius < 0:
                continue

            # When an expanding ring is centered on the bottom boundary, its
            # next visible phase advances one cell along that boundary.
            if color == 5 and center_row == height - 1:
                center_col += 1

            for row,col in {(ring_row,ring_col) for ring_row in range(height) for ring_col in range(width) if abs(ring_row-center_row)+abs(ring_col-center_col)==new_radius}:
                output[row][col] = color

    return output

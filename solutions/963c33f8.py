def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    output = [row[:] for row in grid]

    signal = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] != background and grid[r][c] != 5:
                signal.append((r, c))
    top = min(r for r, c in signal)
    bottom = max(r for r, c in signal)
    left = min(c for r, c in signal)
    right = max(c for r, c in signal)
    length = bottom - top + 1

    for r, c in signal:
        output[r][c] = background

    for source_c in range(left, right + 1):
        column = [grid[r][source_c] for r in range(top, bottom + 1)]
        target_c = source_c

        if column[-1] == 1:
            obstacle = height
            for r in range(bottom + 1, height):
                if grid[r][source_c] == 5:
                    obstacle = r
                    break
            target_top = obstacle - length
        else:
            target_top = height - length
            touched = None
            for r in range(target_top, height):
                if grid[r][source_c] == 5:
                    touched = (r, source_c)
                    break
            if touched is not None:
                remaining = {(r, c) for r in range(height) for c in range(width)
                             if grid[r][c] == 5}
                component = set()
                frontier = [touched]
                remaining.discard(touched)
                while frontier:
                    r, c = frontier.pop()
                    component.add((r, c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr != 0 or dc != 0:
                                neighbor = (r + dr, c + dc)
                                if neighbor in remaining:
                                    remaining.remove(neighbor)
                                    frontier.append(neighbor)
                candidates = []
                for c in {c for r, c in component}:
                    overlap = sum((r, c) in component
                                  for r in range(target_top, height))
                    candidates.append((-overlap, abs(c - source_c), c))
                target_c = min(candidates)[2]

            if grid[height - 1][target_c] == 5:
                right_run = 0
                c = target_c + 1
                while c < width and grid[height - 1][c] == 5:
                    right_run += 1
                    c += 1
                left_run = 0
                c = target_c - 1
                while c >= 0 and grid[height - 1][c] == 5:
                    left_run += 1
                    c -= 1
                direction = 1 if right_run >= left_run else -1
                run = right_run if direction == 1 else left_run
                for step in range(1, min(length, run + 1)):
                    output[height - 1][target_c + direction * step] = background

        for offset, value in enumerate(column):
            output[target_top + offset][target_c] = value

    return output

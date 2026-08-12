def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    colors = sorted({value for row in grid for value in row if value != 0})

    for color in colors:
        unseen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    unseen.add((row, col))
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

        if len(components) != 4:
            continue
        boxes = []
        for component in components:
            boxes.append((
                min(row for row, col in component),
                max(row for row, col in component),
                min(col for row, col in component),
                max(col for row, col in component),
            ))

        for first in range(4):
            for second in range(first + 1, 4):
                top, bottom, left, right = boxes[first]
                other_top, other_bottom, other_left, other_right = boxes[second]
                if top == other_top and bottom == other_bottom:
                    gap_left = min(right, other_right) + 1
                    gap_right = max(left, other_left)
                    for row in range(top, bottom + 1):
                        for col in range(gap_left, gap_right):
                            if grid[row][col] == 0:
                                output[row][col] = color
                if left == other_left and right == other_right:
                    gap_top = min(bottom, other_bottom) + 1
                    gap_bottom = max(top, other_top)
                    for row in range(gap_top, gap_bottom):
                        for col in range(left, right + 1):
                            if grid[row][col] == 0:
                                output[row][col] = color
    return output

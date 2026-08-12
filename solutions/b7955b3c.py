def transform(grid):
    result = [row[:] for row in grid]
    height = len(result)
    width = len(result[0])
    fills = []

    # Treat the azure crosses as missing pixels.  First use rows/columns that
    # agree everywhere the two lines are both visible.
    for i in range(height):
        for j in range(width):
            if result[i][j] != 8:
                continue
            row_donors = []
            for r in range(height):
                if r == i or result[r][j] == 8:
                    continue
                compatible = True
                for c in range(width):
                    if (result[i][c] != 8 and result[r][c] != 8
                            and result[i][c] != result[r][c]):
                        compatible = False
                        break
                if compatible:
                    row_donors.append((abs(i - r), result[r][j], r))
            column_donors = []
            for c in range(width):
                if c == j or result[i][c] == 8:
                    continue
                compatible = True
                for r in range(height):
                    if (result[r][j] != 8 and result[r][c] != 8
                            and result[r][j] != result[r][c]):
                        compatible = False
                        break
                if compatible:
                    column_donors.append((abs(j - c), result[i][c], c))
            row_donors.sort()
            column_donors.sort()
            value = 8
            if row_donors and column_donors:
                if row_donors[0][1] == column_donors[0][1]:
                    value = row_donors[0][1]
                elif row_donors[0][0] < column_donors[0][0]:
                    value = row_donors[0][1]
                elif column_donors[0][0] < row_donors[0][0]:
                    value = column_donors[0][1]
            elif row_donors:
                value = row_donors[0][1]
            elif column_donors:
                value = column_donors[0][1]
            if value != 8:
                fills.append((i, j, value))

    for i, j, value in fills:
        result[i][j] = value

    # Resolve the few still-ambiguous connected gaps from an immutable snapshot,
    # so restoring one cross cannot bias a different cross on the same row.
    visible = [row[:] for row in result]
    seen = []
    final_fills = []
    for start_i in range(height):
        for start_j in range(width):
            if visible[start_i][start_j] != 8 or (start_i, start_j) in seen:
                continue
            component = []
            stack = [(start_i, start_j)]
            seen.append((start_i, start_j))
            while stack:
                i, j = stack.pop()
                component.append((i, j))
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni = i + di
                    nj = j + dj
                    if (0 <= ni < height and 0 <= nj < width
                            and visible[ni][nj] == 8
                            and (ni, nj) not in seen):
                        seen.append((ni, nj))
                        stack.append((ni, nj))

            values = []
            for i, j in component:
                donors = []
                for r in range(height):
                    if r == i or visible[r][j] == 8:
                        continue
                    mismatches = 0
                    for c in range(width):
                        if (visible[i][c] != 8 and visible[r][c] != 8
                                and visible[i][c] != visible[r][c]):
                            mismatches += 1
                    donors.append((mismatches, abs(i - r), visible[r][j], r))
                donors.sort()
                if donors:
                    values.append(donors[0][2])
                else:
                    donors = []
                    for c in range(width):
                        if c == j or visible[i][c] == 8:
                            continue
                        mismatches = 0
                        for r in range(height):
                            if (visible[r][j] != 8 and visible[r][c] != 8
                                    and visible[r][j] != visible[r][c]):
                                mismatches += 1
                        donors.append((mismatches, abs(j - c), visible[i][c], c))
                    donors.sort()
                    values.append(donors[0][2])

            same_row = True
            for i, j in component:
                if i != component[0][0]:
                    same_row = False
            left = min(j for i, j in component)
            right = max(j for i, j in component)
            row = component[0][0]
            if (same_row and left > 0 and right + 1 < width
                    and visible[row][left - 1] == visible[row][right + 1]
                    and visible[row][left - 1] != 8):
                values = [visible[row][left - 1] for cell in component]
            else:
                boundary_counts = {}
                donor_cost = 0
                for index, (i, j) in enumerate(component):
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        neighbor = (i + di, j + dj)
                        if not (0 <= neighbor[0] < height
                                and 0 <= neighbor[1] < width):
                            continue
                        if neighbor in component:
                            other = component.index(neighbor)
                            if other > index and values[index] != values[other]:
                                donor_cost += 1
                        elif visible[neighbor[0]][neighbor[1]] != 8:
                            color = visible[neighbor[0]][neighbor[1]]
                            boundary_counts[color] = boundary_counts.get(color, 0) + 1
                            if values[index] != color:
                                donor_cost += 1
                if boundary_counts:
                    maximum = max(boundary_counts.values())
                    winners = [color for color in boundary_counts
                               if boundary_counts[color] == maximum]
                    uniform_cost = sum(boundary_counts.values()) - maximum
                    if len(winners) == 1 and uniform_cost < donor_cost:
                        values = [winners[0] for cell in component]

            for index, (i, j) in enumerate(component):
                final_fills.append((i, j, values[index]))

    for i, j, value in final_fills:
        result[i][j] = value
    return result

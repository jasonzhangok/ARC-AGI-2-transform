def transform(grid):
    output = []
    row = 0
    while row < len(grid):
        if all(value == 0 for value in grid[row]):
            output.append([0, 0])
            row += 1
            continue

        band = grid[row:row + 2]
        panels = []
        col = 0
        while col < len(grid[0]):
            if band[0][col] == 0 and band[1][col] == 0:
                col += 1
                continue
            left = col
            while (
                col < len(grid[0])
                and not (band[0][col] == 0 and band[1][col] == 0)
            ):
                col += 1
            panels.append([line[left:col] for line in band])

        first, second = next(
            (i, j)
            for i in range(3)
            for j in range(i + 1, 3)
            if set(panels[i][0] + panels[i][1])
            == set(panels[j][0] + panels[j][1])
        )
        target = 3 - first - second

        mappings = []
        for source in (panels[first], panels[second]):
            forward = {}
            reverse = {}
            valid = True
            for source_row, target_row in zip(source, panels[target]):
                for source_color, target_color in zip(source_row, target_row):
                    if (source_color in forward and forward[source_color] != target_color
                            or target_color in reverse and reverse[target_color] != source_color):
                        valid = False
                    forward[source_color] = target_color
                    reverse[target_color] = source_color
            mappings.append(forward if valid else None)
        mapping = mappings[0]
        if mapping is not None:
            pattern = panels[second]
        else:
            mapping = mappings[1]
            pattern = panels[first]

        output.extend(
            [[mapping[value] for value in pattern_row] for pattern_row in pattern]
        )
        row += 2

    return output

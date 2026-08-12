def transform(grid):
    def color_mapping(source, target):
        forward = {}
        reverse = {}
        for source_row, target_row in zip(source, target):
            for source_color, target_color in zip(source_row, target_row):
                if (
                    source_color in forward
                    and forward[source_color] != target_color
                ):
                    return None
                if (
                    target_color in reverse
                    and reverse[target_color] != source_color
                ):
                    return None
                forward[source_color] = target_color
                reverse[target_color] = source_color
        return forward

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

        mapping = color_mapping(panels[first], panels[target])
        if mapping is not None:
            pattern = panels[second]
        else:
            mapping = color_mapping(panels[second], panels[target])
            pattern = panels[first]

        output.extend(
            [[mapping[value] for value in pattern_row] for pattern_row in pattern]
        )
        row += 2

    return output

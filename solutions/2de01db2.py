def transform(grid):
    output = []
    for row in grid:
        counts = {}
        order = []
        for color in row:
            if color != 0:
                if color not in counts:
                    counts[color] = 0
                    order.append(color)
                counts[color] += 1

        main_color = order[0]
        for color in order[1:]:
            if counts[color] > counts[main_color]:
                main_color = color

        output.append([
            0 if color == main_color else main_color
            for color in row
        ])
    return output

def transform(grid):
    h, w = (len(grid), len(grid[0]))
    lines = grid if h > w else [[grid[r][c] for r in range(h)] for c in range(w)]
    dominant = [max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in line] and count_dict), key=count_dict.get) for line in lines]
    sequence = []
    for color in dominant:
        if not sequence or sequence[-1] != color:
            sequence.append(color)
    output = [[v] for v in sequence] if h > w else [sequence]
    return output

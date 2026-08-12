def transform(grid):
    counts = {}
    for cell_value in (v for row in grid for v in row if v != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    size = max(counts.values())
    colors = [v for v, n in counts.items() if n == size]
    colors = [_record_1[2] for _record_1 in sorted(((min((c for row in grid for c, x in enumerate(row) if x == _item_1)), _index_1, _item_1) for _index_1, _item_1 in enumerate(colors)))]
    output = [colors[:] for _ in range(size)]
    return output

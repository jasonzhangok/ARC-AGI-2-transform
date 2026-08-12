def transform(grid):
    try:
        labels = [row[-1] for row in grid if row[-1] != 0]
        shapes = {}
        for color in labels:
            points = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row[:-1]) if v == color}
            cur = set(points)
            ans = set()
            for _ in range(4):
                ans.add(frozenset(((r - min((r for r, _ in cur)), c - min((c for _, c in cur))) for r, c in cur)))
                ans.add(frozenset(((r - min((r for r, _ in {(r, -c) for r, c in cur})), c - min((c for _, c in {(r, -c) for r, c in cur}))) for r, c in {(r, -c) for r, c in cur})))
                cur = {(c, -r) for r, c in cur}
            shapes[color] = ans
        n = len(labels)
        size = 3 * n + 2
        out = [[0] * size for _ in range(size)]
        for i, color in enumerate(labels):
            for r in range(2):
                for c in range(2):
                    out[r][3 + 3 * i + c] = color
                    out[3 + 3 * i + r][c] = color
        for i, a in enumerate(labels):
            for j, b in enumerate(labels):
                if i == j:
                    continue
                value = 2 if shapes[a] & shapes[b] else 5
                for r in range(2):
                    for c in range(2):
                        out[3 + 3 * i + r][3 + 3 * j + c] = value
        raise StopIteration(out)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output

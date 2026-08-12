def _components(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < h and 0 <= nc < w
                                and grid[nr][nc] != 0
                                and (nr, nc) not in seen):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
            result.append(component)
    return result


def _rotate(pattern):
    return [list(row) for row in zip(*pattern[::-1])]


def _orientations(pattern):
    result = []
    for start in (pattern, [row[::-1] for row in pattern]):
        current = start
        for _ in range(4):
            if current not in result:
                result.append(current)
            current = _rotate(current)
    return result


def transform(grid):
    components = _components(grid)
    target = max(components, key=len)
    top = min(r for r, _ in target)
    bottom = max(r for r, _ in target)
    left = min(c for _, c in target)
    right = max(c for _, c in target)
    out = [row[left:right + 1] for row in grid[top:bottom + 1]]
    h, w = len(out), len(out[0])
    holes = {(r, c) for r in range(h) for c in range(w) if out[r][c] == 0}

    patterns = []
    for component in components:
        if component is target:
            continue
        ctop = min(r for r, _ in component)
        cbottom = max(r for r, _ in component)
        cleft = min(c for _, c in component)
        cright = max(c for _, c in component)
        patterns.append([row[cleft:cright + 1]
                         for row in grid[ctop:cbottom + 1]])

    choices = []
    for pattern in patterns:
        candidates = []
        for oriented in _orientations(pattern):
            ph, pw = len(oriented), len(oriented[0])
            mask = {(r, c) for r in range(ph) for c in range(pw)
                    if oriented[r][c] == 2}
            for dr in range(h - ph + 1):
                for dc in range(w - pw + 1):
                    shifted = {(r + dr, c + dc) for r, c in mask}
                    accents_on_target = all(
                        out[dr + r][dc + c] == 2
                        for r in range(ph) for c in range(pw)
                        if oriented[r][c] not in (0, 2))
                    if shifted <= holes and accents_on_target:
                        margin = min(dr, dc, h - dr - ph, w - dc - pw)
                        candidates.append((oriented, dr, dc, shifted, margin))
        choices.append(candidates)

    complete = []

    def assign(index, covered, selected, score):
        if index == len(choices):
            if covered == holes:
                complete.append((score, selected[:]))
            return
        for candidate in choices[index]:
            if not (candidate[3] & covered):
                assign(index + 1, covered | candidate[3],
                       selected + [candidate], score + candidate[4])

    assign(0, set(), [], 0)
    selected = max(complete, key=lambda item: item[0])[1]
    for pattern, dr, dc, _, _ in selected:
        for r, row in enumerate(pattern):
            for c, value in enumerate(row):
                if value:
                    out[dr + r][dc + c] = value
    return out

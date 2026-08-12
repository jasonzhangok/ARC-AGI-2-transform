def transform(grid):
    grid_height, grid_width = len(grid), len(grid[0])
    seen = set()
    components = []
    for r in range(grid_height):
        for c in range(grid_width):
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
                        if (0 <= nr < grid_height and 0 <= nc < grid_width
                                and grid[nr][nc] != 0
                                and (nr, nc) not in seen):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
            components.append(component)
    target = max((len(component),-index,component) for index,component in enumerate(components))[2]
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
        orientations=[]
        for start in (pattern,[row[::-1] for row in pattern]):
            current=start
            for _ in range(4):
                if current not in orientations:orientations.append(current)
                current=[list(row) for row in zip(*current[::-1])]
        for oriented in orientations:
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

    complete=[];stack=[(0,set(),[],0)]
    while stack:
        index,covered,partial,score=stack.pop()
        if index==len(choices):
            if covered==holes:complete.append((score,partial))
            continue
        for candidate in reversed(choices[index]):
            if not candidate[3]&covered:
                stack.append((index+1,covered|candidate[3],partial+[candidate],score+candidate[4]))
    selected=max((item[0],-index,item[1]) for index,item in enumerate(complete))[2]
    for pattern, dr, dc, _, _ in selected:
        for r, row in enumerate(pattern):
            for c, value in enumerate(row):
                if value:
                    out[dr + r][dc + c] = value
    output=out
    return output

def transform(grid):
    h, w = len(grid), len(grid[0])
    candidates = []
    for pr in range(1, h + 1):
        for pc in range(1, w + 1):
            valid = True
            for rr in range(pr):
                for cc in range(pc):
                    reliable = {grid[r][c]
                                for r in range(rr, h, pr)
                                for c in range(cc, w, pc)
                                if grid[r][c] != 1}
                    if len(reliable) > 1:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                candidates.append((pr * pc, pr, pc))
    _, pr, pc = min(candidates)
    template = [[1] * pc for _ in range(pr)]
    for rr in range(pr):
        for cc in range(pc):
            reliable = [grid[r][c]
                        for r in range(rr, h, pr)
                        for c in range(cc, w, pc)
                        if grid[r][c] != 1]
            if reliable:
                template[rr][cc] = reliable[0]
    return [[template[r % pr][c % pc] for c in range(w)] for r in range(h)]

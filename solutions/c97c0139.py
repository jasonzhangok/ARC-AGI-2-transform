def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for seed_r in range(h):
        for seed_c in range(w):
            if grid[seed_r][seed_c] != 2 or (seed_r, seed_c) in seen:
                continue
            stack, twos = [(seed_r, seed_c)], []
            seen.add((seed_r, seed_c))
            while stack:
                r, c = stack.pop()
                twos.append((r, c))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 2 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            if len({r for r, _ in twos}) == 1:
                center_r = float(twos[0][0])
                center_c = (min(c for _, c in twos) + max(c for _, c in twos)) / 2
                radius = (max(c for _, c in twos) - min(c for _, c in twos)) / 2
            else:
                center_r = (min(r for r, _ in twos) + max(r for r, _ in twos)) / 2
                center_c = float(twos[0][1])
                radius = (max(r for r, _ in twos) - min(r for r, _ in twos)) / 2
            for r in range(h):
                for c in range(w):
                    if abs(r - center_r) + abs(c - center_c) <= radius and grid[r][c] == 0:
                        output[r][c] = 8
    return output

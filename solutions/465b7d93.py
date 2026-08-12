from collections import Counter, deque


def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    background = Counter(v for row in grid for v in row).most_common(1)[0][0]
    colors = [v for v in set(v for row in grid for v in row) if v != background]
    frame_color = max(colors, key=lambda v: sum(row.count(v) for row in grid))
    frame = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == frame_color]
    fr0, fr1 = min(r for r, _ in frame), max(r for r, _ in frame)
    fc0, fc1 = min(c for _, c in frame), max(c for _, c in frame)
    signal = [(r, c) for r in range(h) for c in range(w)
              if grid[r][c] not in (background, frame_color)]
    signal_color = grid[signal[0][0]][signal[0][1]]
    sr0, sr1 = min(r for r, _ in signal), max(r for r, _ in signal)
    sc0, sc1 = min(c for _, c in signal), max(c for _, c in signal)
    mask = {(r - sr0, c - sc0) for r, c in signal}
    sh, sw = sr1 - sr0 + 1, sc1 - sc0 + 1
    ir0, ir1, ic0, ic1 = fr0 + 1, fr1 - 1, fc0 + 1, fc1 - 1
    ih, iw = ir1 - ir0 + 1, ic1 - ic0 + 1
    for r, c in signal:
        out[r][c] = background
    if len(mask) == sh * sw:
        for r in range(ir0, ir1 + 1):
            for c in range(ic0, ic1 + 1):
                out[r][c] = signal_color
        return out

    def mapped(y, x):
        ry = 0 if sh == 1 else round(y * (ih - 1) / (sh - 1))
        rx = 0 if sw == 1 else round(x * (iw - 1) / (sw - 1))
        return ir0 + ry, ic0 + rx

    for y, x in mask:
        r, c = mapped(y, x)
        out[r][c] = signal_color
        if (y, x + 1) in mask:
            _, c2 = mapped(y, x + 1)
            for cc in range(min(c, c2), max(c, c2) + 1):
                out[r][cc] = signal_color
        if (y + 1, x) in mask:
            r2, _ = mapped(y + 1, x)
            for rr in range(min(r, r2), max(r, r2) + 1):
                out[rr][c] = signal_color
    return out

def transform(grid):
    h,w=len(grid),len(grid[0]); out=[row[:] for row in grid]
    vr=max(range(w),key=lambda c:sum(grid[r][c]!=0 for r in range(h)))
    hr=max(range(h),key=lambda r:sum(v!=0 for v in grid[r]))
    center=grid[hr][vr]
    for r in range(max(0,hr-1),min(h,hr+2)):
        for c in range(max(0,vr-1),min(w,vr+2)): out[r][c]=4
    out[hr][vr]=center
    return out

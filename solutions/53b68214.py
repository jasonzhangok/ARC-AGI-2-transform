def transform(grid):
    rows=[row[:] for row in grid];w=len(rows[0])
    choice=None
    for lag in range(1,len(rows)):
        for shift in range(-w+1,w):
            if all(rows[r]==([0]*shift+rows[r-lag][:w-shift] if shift>=0 else rows[r-lag][-shift:]+[0]*(-shift)) for r in range(lag,len(rows))):
                choice=(lag,shift);break
        if choice:break
    lag,shift=choice
    while len(rows)<10:
        source=rows[-lag]
        rows.append([0]*shift+source[:w-shift] if shift>=0 else source[-shift:]+[0]*(-shift))
    output=rows
    return output

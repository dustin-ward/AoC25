from sys import stdin
from collections import OrderedDict

lines = []
for line in stdin:
    if line == "\n":
        break
    lines.append(line)
lines.sort()

ranges = OrderedDict()
for line in lines:
    if line == "\n":
        break
    lo,hi = [int(x) for x in line.split('-')]   

    for rlo,rhi in ranges:
        new_lo = rlo
        new_hi = rhi
        if lo < rlo:
            if hi >= rlo:
                new_lo = lo
                new_hi = max(new_hi, hi)
                ranges.pop((rlo,rhi))
                break
        elif lo >= rlo and lo <= rhi:
            new_hi = max(new_hi, hi)
            ranges.pop((rlo,rhi))
            break
    else:
        new_lo = lo
        new_hi = hi
    ranges[(new_lo,new_hi)] = True

ans = 0
for lo,hi in ranges:
    ans += (hi-lo)+1
print(ans)
    

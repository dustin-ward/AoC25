from collections import OrderedDict
import textwrap
R = OrderedDict.fromkeys([tuple([int(x) for x in r.split('-')]) for r in input().split(',')])
ans = 0
for lo, hi in R.keys():
    for x in range(lo, hi+1):
        xs = str(x)
        for k in range(1, (len(xs)//2)+1):
            if len(xs) % k == 0:
                pts = textwrap.wrap(xs, k)
                if all([n == pts[0] for n in pts]):
                    ans += x
                    break
print(ans)

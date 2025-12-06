from collections import OrderedDict
R = OrderedDict.fromkeys([tuple([int(x) for x in r.split('-')]) for r in input().split(',')])
ans = 0
for x in range(1,100000):
    xx = int(str(x) + str(x))
    for lo,hi in R.keys():
        if xx >= lo and xx <= hi:
            ans+=xx
print(ans)

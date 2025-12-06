from sys import stdin
ans = 0
for line in stdin:
    d1 = max(line[:-2])
    d2 = max(line[line.index(d1)+1:])
    ans += int(d1+d2)
print(ans)

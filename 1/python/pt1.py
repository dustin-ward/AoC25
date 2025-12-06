from sys import stdin

dial = 50
ans = 0
for line in stdin:
    d = line[0]
    n = int(line[1:])
    if d == 'L':
        dial = (dial+100 - n) % 100
    else:
        dial = (dial+100 + n) % 100
    if dial == 0:
        ans += 1
print(ans)

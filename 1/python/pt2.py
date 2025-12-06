from sys import stdin

dial = 50
ans = 0
for line in stdin:
    d = line[0]
    n = int(line[1:])
    
    mul = n // 100
    ans += mul
    n = n % 100
    n = -n if d == 'L' else n

    if dial != 0 and (dial + n < 0 or dial + n > 100):
        ans += 1

    dial = ((dial + 100) + n) % 100
    if dial == 0:
        ans += 1

print(ans)

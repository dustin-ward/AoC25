from sys import stdin
ans = 0
for line in stdin:
    d = []
    end = -12
    for i in range(12):
        xd = max(line[:end])
        line = line[line.index(xd)+1:]
        d.append(xd)
        end += 1
    ans += int(''.join(d))
print(ans)

from sys import stdin
ranges = {}
for line in stdin:
    if line == "\n":
        break
    lo,hi = [int(x) for x in line.split('-')]   
    ranges[(lo,hi)] = True
ans = 0
for line in stdin:
    x = int(line)
    for lo,hi in ranges:
        if x >= lo and x <= hi:
            ans +=1
            break

print(ans)

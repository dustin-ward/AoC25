from sys import stdin

pts = []
for line in stdin:
    x, y = [int(x) for x in line.split(',')]
    pts.append((x, y))

ans = 0
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        area = abs(pts[i][0]-pts[j][0]+1) * abs(pts[i][1]-pts[j][1]+1)
        ans = max(ans, area)

print(ans)

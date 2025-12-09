from sys import stdin
from shapely.geometry import Polygon

pts = []
for i, line in enumerate(stdin):
    x, y = [int(x) for x in line.split(',')]
    pts.append((x, y))

poly = Polygon(pts)

ans = 0
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        x1, y1 = min(pts[i][0], pts[j][0]), min(pts[i][1], pts[j][1])
        x2, y2 = max(pts[i][0], pts[j][0]), max(pts[i][1], pts[j][1])

        rect = Polygon([
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1),
        ])

        if poly.buffer(1e-13).contains(rect):
            area = (abs(pts[i][0]-pts[j][0])+1) * (abs(pts[i][1]-pts[j][1])+1)
            ans = max(ans, area)

print(ans)

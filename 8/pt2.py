class UnionFind():
    def __init__(self, n):
        self.n = n
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)

        if x_p == y_p:
            return False

        if self.r[x_p] > self.r[y_p]:
            self.p[y_p] = x_p
        elif self.r[x_p] < self.r[y_p]:
            self.p[x_p] = y_p
        else:
            self.p[y_p] = x_p
            self.r[x_p] += 1

        return True

from sys import stdin
pts = []
for line in stdin:
    x,y,z = [int(x) for x in line.split(',')]
    pts.append((x,y,z))

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

distances = []
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        distances.append((i,j,dist(pts[i],pts[j])))

distances.sort(key=lambda x: x[2])

ans = 0
uf = UnionFind(len(pts))
last = 0
for x in range(len(distances)):
    i,j,d = distances[x]
    merged = uf.merge(i,j)
    if merged:
        last = x

i,j,_ = distances[last]
print(pts[i][0]*pts[j][0])

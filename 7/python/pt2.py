from sys import stdin
from functools import cache

grid = [line.strip() for line in stdin]
N = len(grid)
M = len(grid[0])
start_j = grid[0].index("S")

V = []
for _ in range(N):
    V.append([0]*M)


@cache
def f(i, j):
    if i >= N or j < 0 or j >= M:
        return 1
    x = 0
    if grid[i][j] == '^':
        x += f(i, j+1)
        x += f(i, j-1)
    else:
        x += f(i+1, j)
    return x


print(f(0, start_j))

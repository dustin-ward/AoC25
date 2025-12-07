from sys import stdin

grid = [line.strip() for line in stdin]
N = len(grid)
M = len(grid[0])

start_j = grid[0].index("S")

V = []
for _ in range(N):
    V.append([0]*M)


def f(i, j):
    if i >= N or j < 0 or j >= M:
        return
    if V[i][j] != 0:
        return
    if grid[i][j] == '^':
        V[i][j] = 1
        f(i,j+1)
        f(i,j-1)
    else:
        f(i+1,j)

f(0, start_j)

ans = 0
for i,r in enumerate(V):
    # print(f'r={i}, sum={sum(r)}')
    ans += sum(r)
print(ans)

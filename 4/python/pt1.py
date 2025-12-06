from sys import stdin
G = [line for line in stdin]
N = len(G)
M = len(G[0])
ans = 0

dy = [-1,-1,-1,0,1,1,1,0]
dx = [-1,0,1,1,1,0,-1,-1]

def bounds(i,j):
    return i>=0 and i<N and j>=0 and j<M

for i in range(N):
    for j in range(M):
        if G[i][j] == '@':
            adj = 0
            for k in range(8):
                ii = i+dy[k]
                jj = j+dx[k]
                if bounds(ii,jj) and G[ii][jj] == '@':
                    adj += 1
            if adj < 4:
                ans+=1
print(ans)

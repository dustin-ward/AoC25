from sys import stdin

ops = ['*', '+']

probs = []
for line in stdin:
    line = line.strip()
    nums = [l for l in line.split(' ') if l != '']
    probs.append([int(x) if x not in ops else x for x in nums])

ans = 0

for i in range(len(probs[0])):
    x = probs[0][i]
    for j in range(1, len(probs)-1):
        if probs[-1][i] == '*':
            x *= probs[j][i]
        else:
            x += probs[j][i]
    ans += x
print(ans)


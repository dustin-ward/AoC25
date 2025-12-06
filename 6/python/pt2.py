from sys import stdin

ops = ['*', '+']

probs = []
for line in stdin:
    probs.append(line[:-1])

ans = 0

nums = []
for i in range(len(probs[0])-1, -1, -1):
    op = None
    if probs[-1][i] in ops:
        op = probs[-1][i]

    cur_num = []
    for j in range(len(probs)-2, -1, -1):
        if probs[j][i] != ' ':
            cur_num.insert(0, probs[j][i])
    if len(cur_num) == 0:
        continue
    nums.append(int(''.join(cur_num)))

    if op:
        if op == '*':
            x = 1
            for n in nums:
                x *= n
        if op == '+':
            x = 0
            for n in nums:
                x += n
        ans += x
        nums = []
print(ans)

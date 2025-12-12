from sys import stdin

shapes = {}

lines = [x for x in stdin]

for i in range(6):
    idx = i*5
    shapeno = int(lines[idx][0])
    count = lines[idx+1].count("#")
    count += lines[idx+2].count("#")
    count += lines[idx+3].count("#")
    shapes[shapeno] = count

idx = 6*5
ans = 0
for l in lines[idx:]:
    size, nums = l.strip().split(':')
    n, m = [int(x) for x in size.split('x')]
    nums = [int(x) for x in nums.strip().split(' ')]
    if sum(nums*7) <= n*m:
        ans += 1

print(ans)

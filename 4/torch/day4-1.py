import torch

class Day4Model(torch.nn.Module):
    def __init__(self, convs):
        super().__init__()
        self.convs = convs
        self.kernel = torch.tensor(
            [[[[1,1,1],
               [1,0,1],
               [1,1,1]]]]
        )

    def forward(self, x):
        y = torch.reshape(x, (1,1,*x.shape))

        for layer in range(self.convs):
            sums = torch.conv2d(y, self.kernel, padding="same")
            y = torch.where(torch.gt(sums, 3), y, torch.zeros(y.shape))

        return torch.sum(x) - torch.sum(y)


from sys import stdin
grid = []
for line in stdin:
    line = line.strip()
    grid.append([1 if c == '@' else 0 for c in line])


model = Day4Model(1)
input = torch.tensor(grid)
ans = model(input)
print(int(ans.item()))

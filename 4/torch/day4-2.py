import torch

class Day4Model(torch.nn.Module):
    def __init__(self, convs):
        super().__init__()
        self.convs = convs
        self.kernel = torch.tensor(
            [[[[1.,1.,1.],
               [1.,0.,1.],
               [1.,1.,1.]]]]
        ).cuda()

    def forward(self, x):
        y = torch.reshape(x, (1,1,*x.shape))

        for layer in range(self.convs):
            sums = torch.conv2d(y, self.kernel, padding="same")
            y = torch.where(torch.gt(sums, 3), y, torch.zeros(y.shape).cuda())

        return torch.sum(x) - torch.sum(y)

# READ INPUT

from sys import stdin
grid = []
rolls = 0
for line in stdin:
    line = line.strip()
    grid.append([1 if c == '@' else 0 for c in line])
    rolls += line.count('@')

# INFERENCE

model = Day4Model(rolls//100).cuda()
input = torch.tensor(grid, dtype=torch.float32).cuda()
ans = model(input)
print(int(ans.item()))

# torch.onnx.export(model, (input,), 'day4.onnx', input_names=['x'], dynamo=True)

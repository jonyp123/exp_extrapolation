import torch
import torch.nn as nn
import random

x = []
y = []
for number in range(1000):
	x1 = random.randrange(1,10000)
	x2 = random.randrange(1,10000)
	x.append([float(x1/1000), float(x2/1000)])
	y.append([float(x1/1000)**2 + float(x2/1000)**2])

x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

model = nn.Sequential(
    nn.Linear(2, 4),
    nn.ReLU(),
    nn.Linear(4, 1)
)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(3000):
    prediction = model(x)

    loss = loss_fn(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 300 == 0:
        print(epoch, loss.item())

test = torch.tensor([[10.0, 20.0]])
print(model(test))
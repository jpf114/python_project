import torch
from torch import nn

inputs = torch.tensor([1, 2, 3], dtype=torch.float)
targets = torch.tensor([1, 2, 5], dtype=torch.float)

inputs = torch.reshape(inputs, (1, 1, 1, 3))
targets = torch.reshape(targets, (1, 1, 1, 3))

loss_L1 = nn.L1Loss(reduction='mean')
result = loss_L1(inputs, targets)
print(result)

loss_MSE = nn.MSELoss(reduction='mean')
result = loss_MSE(inputs, targets)
print(result)
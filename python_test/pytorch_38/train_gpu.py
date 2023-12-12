import time

import torch.utils.data
import torchvision.datasets
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# from pytorch_38.model_class import model_class1

# 数据集准备
train_data = torchvision.datasets.CIFAR10("data", train=True, transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10("data", train=False, transform=torchvision.transforms.ToTensor(),
                                         download=True)

train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练数据集大小 ：{}，测试数据集大小：{}".format(train_data_size, test_data_size))

train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

Device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 创建网络模型
class model_class1(nn.Module):
    def __init__(self):
        super(model_class1, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x


model_c1 = model_class1()
model_c1.to(Device)

# 损失函数
loss_fn = nn.CrossEntropyLoss()
loss_fn.to(Device)

# 优化器
learn_rate = 0.01
optim = torch.optim.SGD(model_c1.parameters(), lr=learn_rate)

# 设置网络模型的一些参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 30

writer = SummaryWriter("log")

for i in range(epoch):
    print("------------第{}轮训练-------------".format(i + 1))
    start_time = time.time()
    # 训练步骤开始
    model_c1.train()
    for tra_data in train_dataloader:
        imgs, targets = tra_data
        imgs = imgs.to(Device)
        targets = targets.to(Device)
        output = model_c1(imgs)
        loss = loss_fn(output, targets)

        # 优化器优化模型
        optim.zero_grad()
        loss.backward()
        optim.step()

        total_train_step = total_train_step + 1
        if total_train_step % 100 == 0:
            end_time = time.time()
            print("训练次数：{}，loss：{}".format(total_train_step, round(loss.item(), 4)))
            print("消耗时间：{} s".format(round(end_time - start_time, 4)))
            writer.add_scalar('train_loss', loss.item(), total_train_step)

    # 测试步骤开始
    total_test_loss = 0
    total_accuracy = 0
    model_c1.eval()
    with torch.no_grad():
        for tes_data in test_dataloader:
            imgs, targets = tes_data
            imgs = imgs.to(Device)
            targets = targets.to(Device)
            output = model_c1(imgs)
            loss = loss_fn(output, targets)
            total_test_loss = total_test_loss + loss.item()
            accuracy = (output.argmax(1) == targets).sum()
            total_accuracy = total_accuracy + accuracy

    print("整体测试集上的loss：{}".format(round(total_test_loss, 4)))
    print("整体测试集上的正确率：{}%".format(total_accuracy / test_data_size))
    writer.add_scalar('test_loss', total_test_loss, total_test_step)
    writer.add_scalar('test_accuracy', total_accuracy / test_data_size, total_test_step)
    total_test_step = total_test_step + 1

    torch.save(model_c1, "model/model_c1_{}.pth".format(i))
    print("模型已保存")

writer.close()

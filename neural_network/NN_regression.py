import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-1, 1, 200), dim=1)
y = x.pow(2)*2 + 0.2*torch.rand(x.size())-1
x, y = torch.autograd.Variable(x), torch.autograd.Variable(y)

plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()


lr = 0.1

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # 定義神經層的特性
        self.linear1 = torch.nn.Linear(1, 10)
        self.linear2 = torch.nn.Linear(10, 6)
        self.linear3 = torch.nn.Linear(6, 4)
        self.linear4 = torch.nn.Linear(4, 1)

    def forward(self, x):
        # 神經網路架構在此決定
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        x = self.linear4(x)
        return x


net = Net()
optimizer = torch.optim.SGD(net.parameters(), lr=lr)
loss_func = torch.nn.MSELoss()

plt.ion()
plt.show()

for t in range(3000):
    prediction = net(x)
    loss = loss_func(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if t % 5 ==0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, f'epoch: {t}\nLoss={round(float(loss.data),4)}', fontdict={'size':20, 'color':'red'})
        plt.pause(0.05)

plt.ioff()
plt.show()
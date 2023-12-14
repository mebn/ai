import torch
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

# data
train = datasets.MNIST("../data", train=True, download=True, transform=transforms.ToTensor())
test = datasets.MNIST("../data", train=False, download=True, transform=transforms.ToTensor())

# set
trainset = torch.utils.data.DataLoader(train, batch_size=64, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=64, shuffle=True)


import torch
import torchvision
from torchvision import transforms, datasets

# data
train = datasets.MNIST("../data", train=True, download=True, transform=transforms.ToTensor())
test = datasets.MNIST("../data", train=False, download=True, transform=transforms.ToTensor())


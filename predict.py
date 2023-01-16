'''Train CIFAR10 with PyTorch.'''
import torch
import torch.nn as nn

import torch.nn.functional as F
import torch.backends.cudnn as cudnn

import torchvision
import torchvision.transforms as transforms

import os

from models import *
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import time

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'device: {device}')

# Data
print('==> Preparing data..')
mean = np.array([0.4914, 0.4822, 0.4465])
std =  np.array([0.2023, 0.1994, 0.2010])
transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean, std),
])

testset = torchvision.datasets.CIFAR10(
    root='./data', train=False, download=True, transform=transform_test)

testloader = torch.utils.data.DataLoader(
    testset, batch_size=4, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck')

# Model
print('==> Building model..')
net = VGG('VGG19')

net = net.to(device)
if device == 'cuda':
    net = torch.nn.DataParallel(net)
    cudnn.benchmark = True

# Load checkpoint
checkpoint = torch.load('./checkpoint/ckpt.pth')
net.load_state_dict(checkpoint['net'])
best_acc = checkpoint['acc']
start_epoch = checkpoint['epoch']

def imshow(sample):
    denormalize=transforms.Normalize((-1*mean/std),(1.0/std))
    sample=denormalize(sample).squeeze()
    
    sample=sample.cpu().permute(1,2,0)
    print(sample.size())
    
    plt.title('fps: {:.2f}sec'.format(T), loc='left')
    plt.imshow(sample)
    plt.show()
    plt.savefig('./sample.png')

for batch_idx, (inputs, targets) in enumerate(testloader):
    inputs, targets = inputs.to(device), targets.to(device)
    
    start=time.time()
    outputs = net(inputs)
    T=time.time()-start

    # print(f'inputs: {inputs.size()}')
    # print(f'targets: {targets.size()}')
    # print(f'outputs: {outputs.size()}')

    print(f'targets: {targets}')
    print(f'outputs: {torch.argmax(outputs, dim=1)}')
    
    idx=0
    sample = inputs[idx]
    target = targets[idx]
    output = torch.argmax(outputs, dim=1)[idx]

    print(f'sample: {sample.size()}')    
    print(f'targets: {target}: {classes[target]}')
    print(f'output: {output}: {classes[output]}')

    imshow(sample)
    
    break








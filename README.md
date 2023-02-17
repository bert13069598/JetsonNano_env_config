# JetsonNano
<img src= "https://github.com/bert13069598/JetsonNano/blob/master/JetsonNano.png">

## Download SD Card Image
[Jetson Download Center](https://developer.nvidia.com/embedded/downloads)
NVIDIA Jetson Nano 2GB Developer Kit
|||
| :--------: | :--------: |
| Architecture | aarch64 |
| JetPack | 4.6.1 |
| CUDA | 10.2.300 |
| cuDNN | 8.2.1.32 |
| Python3 | 3.6.9 |



## Write Image to the microSD Card
[Formatter&Etcher](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#write)

<!--
## Install Anaconda
wget http://github.com/seibert/jetconda/releases/download/v1.0.0-tx2/Jetconda3-1.0.0-Linux-aarch64.sh
-->

## Train CIFAR10 with PyTorch
[Pytorch for jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
### torch 1.8.0
```bash
wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-1.8.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev
pip3 install Cython
pip3 install numpy torch-1.8.0-cp36-cp36m-linux_aarch64.whl
```
### torchvision 0.9.0
```bash
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
git clone --branch v0.9.0 https://github.com/pytorch/vision torchvision   # see below for version of torchvision to download
cd torchvision
export BUILD_VERSION=0.9.0  # where 0.x.0 is the torchvision version  
python3 setup.py install --user
```
##
[Pytorch-cifar10](https://github.com/kuangliu/pytorch-cifar)
```bash
pip3 install image
```

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

![image](https://user-images.githubusercontent.com/89738612/228831090-748374bd-1893-4f35-809d-5d5e2505e58c.png)


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
sudo apt install -y python3-pip libopenblas-base libopenmpi-dev libomp-dev
pip3 install Cython
wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-1.8.0-cp36-cp36m-linux_aarch64.whl
pip3 install numpy torch-1.8.0-cp36-cp36m-linux_aarch64.whl
```
### torchvision 0.9.0
```bash
sudo apt install -y libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev git
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

- version check



| ``torch``                | ``torchvision``          | ``python``                      |
| :---: | :---: | :---: |
| ``main`` / ``nightly``   | ``main`` / ``nightly``   | ``>=3.8``, ``<=3.10``           |
| ``1.13.0``               | ``0.14.0``               | ``>=3.7.2``, ``<=3.10``         |
| ``1.12.0``               | ``0.13.0``               | ``>=3.7``, ``<=3.10``           |
| ``1.11.0``               | ``0.12.0``               | ``>=3.7``, ``<=3.10``           |
| ``1.10.2``               | ``0.11.3``               | ``>=3.6``, ``<=3.9``            |
| ``1.10.1``               | ``0.11.2``               | ``>=3.6``, ``<=3.9``            |
| ``1.10.0``               | ``0.11.1``               | ``>=3.6``, ``<=3.9``            |
| ``1.9.1``                | ``0.10.1``               | ``>=3.6``, ``<=3.9``            |
| ``1.9.0``                | ``0.10.0``               | ``>=3.6``, ``<=3.9``            |
| ``1.8.2``                | ``0.9.2``                | ``>=3.6``, ``<=3.9``            |
| ``1.8.1``                | ``0.9.1``                | ``>=3.6``, ``<=3.9``            |
| ``1.8.0``                | ``0.9.0``                | ``>=3.6``, ``<=3.9``            |
| ``1.7.1``                | ``0.8.2``                | ``>=3.6``, ``<=3.9``            |
| ``1.7.0``                | ``0.8.1``                | ``>=3.6``, ``<=3.8``            |
| ``1.7.0``                | ``0.8.0``                | ``>=3.6``, ``<=3.8``            |
| ``1.6.0``                | ``0.7.0``                | ``>=3.6``, ``<=3.8``            |
| ``1.5.1``                | ``0.6.1``                | ``>=3.5``, ``<=3.8``            |
| ``1.5.0``                | ``0.6.0``                | ``>=3.5``, ``<=3.8``            |
| ``1.4.0``                | ``0.5.0``                | ``==2.7``, ``>=3.5``, ``<=3.8`` |
| ``1.3.1``                | ``0.4.2``                | ``==2.7``, ``>=3.5``, ``<=3.7`` |
| ``1.3.0``                | ``0.4.1``                | ``==2.7``, ``>=3.5``, ``<=3.7`` |
| ``1.2.0``                | ``0.4.0``                | ``==2.7``, ``>=3.5``, ``<=3.7`` |
| ``1.1.0``                | ``0.3.0``                | ``==2.7``, ``>=3.5``, ``<=3.7`` |
| ``<=1.0.1``              | ``0.2.2``                | ``==2.7``, ``>=3.5``, ``<=3.7`` |

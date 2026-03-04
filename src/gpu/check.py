#!/usr/bin/python3

# https://colab.research.google.com/drive/1bd52NHDO_KQL0dJbmcQ-YxKWNChYoosN

import time
import tensorflow as tf
import torch

print("Hello, World!\t ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "\n")

# Check TensorFlow and PyTorch versions
print(f"TensorFlow Version: {tf.__version__}")
print(f"PyTorch Version: {torch.__version__}\n")

# Check CUDA versions
!/usr/local/cuda/bin/nvcc --version
print("\n")

# Check GPU devices
!nvidia-smi
print("\n")
!nvidia-smi -L
print("\n")

To check Cuda version:
we can use nvidia-smi or nvcc in linux kernel or cmd
# CUDA and PyTorch Notes

## Check CUDA Version

To check the CUDA version installed on your system:

### Using NVIDIA System Management Interface

```bash
nvidia-smi
```

This shows:
- GPU model
- Driver version
- CUDA version supported by the driver

### Using CUDA Compiler

```bash
nvcc --version
```

or

```bash
nvcc -V
```

This shows the CUDA Toolkit version installed on your computer.

> Note:
> - `nvidia-smi` reports the CUDA version supported by the NVIDIA driver.
> - `nvcc --version` reports the installed CUDA Toolkit version.
> - These versions may be different.

---

# Installing PyTorch

Install the CUDA-enabled version of PyTorch:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

Verify the installation:

```python
import torch

print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
```

---

# What is PyTorch?

PyTorch is an open-source machine learning and deep learning framework developed by Meta.

It is used to:
- Build neural networks
- Train deep learning models
- Perform GPU-accelerated computations
- Work with computer vision, NLP, reinforcement learning, and more

---

# What is a Neural Network?

A neural network is a machine learning model inspired by the human brain.

It consists of:
- Input layer
- One or more hidden layers
- Output layer

Each layer contains neurons connected by weights. During training, these weights are adjusted so the network learns patterns from data.

Example applications:
- Image classification
- Object detection
- Speech recognition
- Language translation
- Chatbots
- Recommendation systems

---

# Relationship

```
GPU
 │
 ├── CUDA (NVIDIA platform)
 │
 └── PyTorch
      │
      └── Neural Networks
             │
             └── Deep Learning Models
```
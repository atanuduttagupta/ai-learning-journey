# Day 35 — PyTorch Foundations & Tensor Operations

![PyTorch](https://img.shields.io/badge/Framework-PyTorch-red)
![Deep Learning](https://img.shields.io/badge/Topic-DeepLearning-blue)
![Level](https://img.shields.io/badge/Level-Beginner-green)

---

# 📌 Overview

This notebook introduces the foundations of **PyTorch**, one of the most popular Deep Learning frameworks used in AI research and production.

The notebook focuses on:

- PyTorch basics
- Tensor fundamentals
- Tensor operations
- Tensor reshaping
- GPU acceleration
- Automatic differentiation (Autograd)
- Hands-on tensor practice

This is the foundation required before learning:
- Neural Networks
- Training Loops
- Optimizers
- Deep Learning Models

---

# 🎯 Learning Objectives

By the end of this notebook, you will be able to:

✅ Understand PyTorch fundamentals  
✅ Create and manipulate tensors  
✅ Perform tensor operations  
✅ Understand tensor dimensions and shapes  
✅ Use GPU acceleration with CUDA  
✅ Understand Autograd and gradients  
✅ Build the base required for Deep Learning

---

# 🧠 Topics Covered

## 1️⃣ Introduction to PyTorch
- What is PyTorch?
- Why PyTorch is popular
- Dynamic computation graphs
- PyTorch ecosystem

---

## 2️⃣ Tensor Fundamentals
- Scalars
- Vectors
- Matrices
- Higher dimensional tensors
- Tensor shapes
- Tensor dimensions

---

## 3️⃣ Tensor Creation
- `torch.tensor()`
- `torch.zeros()`
- `torch.ones()`
- `torch.rand()`
- `torch.randn()`
- `torch.arange()`

---

## 4️⃣ Tensor Operations
- Addition
- Subtraction
- Multiplication
- Division
- Matrix multiplication
- Statistical operations

---

## 5️⃣ Tensor Indexing & Slicing
- Row selection
- Column selection
- Conditional selection
- Boolean masking

---

## 6️⃣ Tensor Reshaping
- `reshape()`
- `view()`
- `unsqueeze()`
- `squeeze()`

---

## 7️⃣ Broadcasting
- Tensor broadcasting rules
- Shape compatibility
- Efficient tensor operations

---

## 8️⃣ NumPy vs PyTorch
- Similarities
- Differences
- GPU support
- Deep learning capabilities

---

## 9️⃣ GPU & CUDA Basics
- CPU vs GPU tensors
- CUDA availability
- Moving tensors to GPU

---

## 🔟 Automatic Differentiation (Autograd)
- `requires_grad=True`
- Computational graphs
- Gradient calculation
- `.backward()`

---

# 🚀 Sample Code

## Tensor Creation

```python
import torch

x = torch.tensor([1,2,3])

print(x)
```

---

## Matrix Multiplication

```python
a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([[5,6],[7,8]])

print(torch.matmul(a,b))
```

---

## Autograd Example

```python
x = torch.tensor(2.0, requires_grad=True)

y = x**2

y.backward()

print(x.grad)
```

---

# 📚 Key Concepts Learned

| Concept | Importance |
|---|---|
| Tensors | Core Deep Learning data structure |
| Tensor Operations | Mathematical computation |
| CUDA | GPU acceleration |
| Autograd | Backpropagation foundation |
| Broadcasting | Efficient tensor computation |

---

# 🧩 Real-World Applications

- Computer Vision
- NLP
- Generative AI
- Deep Learning
- Large Language Models

---

# 📈 Learning Progression

```text
PyTorch Basics
      ↓
Tensor Operations
      ↓
Autograd
      ↓
Neural Networks
      ↓
Training Loops
      ↓
Optimizers
```

---

# 🎓 Final Outcome

After Day 35, you should comfortably understand:

- How tensors work
- Why PyTorch is powerful
- How GPU acceleration helps
- How gradients are calculated
- Deep learning mathematical foundations

---

# 🚀 Happy Learning!

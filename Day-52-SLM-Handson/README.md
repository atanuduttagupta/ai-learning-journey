# Day 52 – Long Context & Small Language Models (SLMs)

## Learning Objectives

- Understand Long Context Windows in modern LLMs
- Learn Small Language Models (SLMs)
- Explore Tool Calling / Function Calling
- Run Local Inference Pipelines
- Understand Edge AI Deployment
- Learn Knowledge Distillation

---

## Topics Covered

### 1. Long Context Models
- Context windows
- Why long context matters
- Attention complexity O(n²)
- Flash Attention
- Sparse Attention
- Sliding Window Attention
- Mamba and State Space Models

### 2. Small Language Models (SLMs)
Examples:
- Phi-3
- TinyLlama
- Gemma
- Qwen

Benefits:
- Faster inference
- Lower cost
- Local deployment
- Better privacy

### 3. SLM vs LLM

| Feature | SLM | LLM |
|----------|----------|----------|
| Parameters | 1B–10B | 70B+ |
| Cost | Low | High |
| Speed | Fast | Slower |
| Hardware | Laptop | GPU Cluster |
| Offline | Yes | Difficult |

### 4. Tool Calling / Function Calling

Workflow:

User → LLM → Tool Selection → Tool Execution → Response

Examples:
- Calculator
- Weather API
- Database Query
- ERP API
- Search Engine

### 5. Local Inference

Popular Tools:
- Ollama
- LM Studio
- llama.cpp
- vLLM
- TGI

Example:

```bash
ollama run tinyllama
```

### 6. Quantization

Model Compression:

FP32 → FP16 → INT8 → INT4

Benefits:
- Lower RAM
- Faster inference
- Edge deployment

### 7. Edge AI

Run models directly on:
- Mobile phones
- Laptops
- Cars
- Cameras
- IoT Devices

Benefits:
- Privacy
- Offline usage
- Low latency

### 8. Knowledge Distillation

Teacher Model → Student Model

Example:

- Teacher: Llama 70B
- Student: TinyLlama

Benefits:
- Smaller size
- Faster inference
- Lower cost

---

## Hands-On Exercises

### Exercise 1: Run TinyLlama in Jupyter

Load TinyLlama using Hugging Face Transformers.

### Exercise 2: Run Phi-3 Mini

Compare outputs against TinyLlama.

### Exercise 3: SLM vs LLM Benchmark

Compare:
- Response quality
- Latency
- Memory usage

### Exercise 4: Tool Calling Demo

Create:
- Calculator Tool
- Weather Tool

Let the model choose which tool to invoke.

### Exercise 5: Ollama API

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model":"tinyllama",
        "prompt":"What is Machine Learning?",
        "stream":False
    }
)
```

---

## Mini Project

### Local AI ERP Assistant

Tools:
- get_employee()
- get_invoice()
- get_customer()
- calculator()

Flow:

User Question
→ TinyLlama / Phi-3
→ Tool Selection
→ Python Function
→ Final Answer

---

## Interview Questions

1. What is a context window?
2. Why are long-context models important?
3. Difference between SLM and LLM?
4. What is tool calling?
5. What is quantization?
6. What is local inference?
7. What is Edge AI?
8. Explain knowledge distillation.
9. Distillation vs Quantization.
10. Design a local AI assistant using SLMs and tools.

---

## Key Takeaway

Large Models
→ Distillation
→ Small Models
→ Quantization
→ Local Inference
→ Edge AI
→ Tool Calling
→ AI Agents

This trend is shaping the future of practical, cost-efficient AI systems.

# Day 49: Reinforcement Learning (RL) and Reinforcement Learning from Human Feedback (RLHF)

## Overview

This notebook explores the foundations of Reinforcement Learning (RL) and the Reinforcement Learning from Human Feedback (RLHF) pipeline used to align modern Large Language Models (LLMs) such as ChatGPT.

## Learning Objectives

- Understand Reinforcement Learning fundamentals
- Learn about rewards, policies, and policy gradients
- Understand positive and negative rewards
- See how random actions become intelligent decisions through reward-based learning
- Learn the RLHF training pipeline
- Understand Pre-Training, Alignment, and Supervised Fine-Tuning (SFT)
- Learn why SFT is expensive
- Understand Reward Models and Human Preference Learning
- Learn the OpenAI Pairwise Preference (Log-Sigmoid) Loss
- Implement hands-on examples using GPT-2 and a simple reward model

---

## Reinforcement Learning Concepts

### Agent and Environment

An agent interacts with an environment by taking actions and receiving rewards.

```text
Agent → Action → Environment → Reward → Agent
```

### Positive and Negative Rewards

- Correct action → Positive reward
- Incorrect action → Negative reward

### Policy

A policy defines which action an agent should take in a given state.

```text
π(a|s)
```

Probability of action `a` given state `s`.

### Policy Gradient

Policy Gradient methods directly optimize the policy.

```text
θ = θ + α × Reward × ∇logπ(a|s)
```

Good actions become more probable.
Bad actions become less probable.

---

## RLHF Pipeline

```text
Internet Data
      ↓
Pre-Training
      ↓
Base GPT
      ↓
Supervised Fine-Tuning (SFT)
      ↓
Reward Model
      ↓
PPO Reinforcement Learning
      ↓
Aligned ChatGPT
```

---

## Pre-Training

The model learns next-token prediction from massive internet datasets.

Loss Function:

```text
Cross Entropy Loss
```

---

## Alignment

Alignment ensures AI systems are:

- Helpful
- Honest
- Safe
- Harmless

---

## Supervised Fine-Tuning (SFT)

Humans create high-quality prompt-response pairs.

Example:

**Prompt**
> How do I learn Python?

**Answer**
> Start with variables, loops, functions, and projects.

### Why is SFT expensive?

Humans must manually create large volumes of responses, making data collection costly and time-consuming.

---

## Reward Model

A Reward Model is trained to predict which responses humans prefer.

Input:

```text
Prompt + Response
```

Output:

```text
Reward Score
```

The reward model acts as a learned human judge.

---

## How Does the Reward Model Learn?

Humans compare two responses:

```text
Prompt

Response A
Response B
```

Humans select:

```text
A Better Than B
```

or

```text
B Better Than A
```

The Reward Model learns:

```text
Preferred Response  → Higher Reward
Rejected Response   → Lower Reward
```

### Important Insight

The Reward Model does NOT learn:

> Which answer is correct?

Instead it learns:

> Which answer would humans prefer?

---

## OpenAI Pairwise Preference Loss

For:

- Chosen Response = yc
- Rejected Response = yr

The reward model predicts:

```text
r(yc)
r(yr)
```

Loss Function:

```text
L = -log(σ(r(yc)-r(yr)))
```

where

```text
σ(x)=1/(1+e^-x)
```

Objective:

```text
Chosen Response   → Higher Reward
Rejected Response → Lower Reward
```

---

## Hands-On Sections

### 1. GPT-2 Text Generation

Generate responses using a pretrained GPT-2 model.

### 2. Human Preference Simulation

Create chosen/rejected response pairs.

### 3. Reward Model Architecture

Build a simple reward model using PyTorch.

### 4. Pairwise Preference Loss

Implement OpenAI's log-sigmoid preference loss.

### 5. Open Source Reward Models

Explore reward models available through Hugging Face.

---

## Mini Project

Build a simplified RLHF pipeline:

1. Generate responses using GPT
2. Create preference rankings
3. Build chosen/rejected datasets
4. Train a reward model
5. Select the highest-reward response

---

## Next Topic (Day 50)

- PPO (Proximal Policy Optimization)
- Value Function
- Advantage Function
- Actor-Critic Architecture
- RLHF Optimization
- DPO (Direct Preference Optimization)

---

## Author

Part of the AI Learning Roadmap Series by Atanu Dutta Gupta.

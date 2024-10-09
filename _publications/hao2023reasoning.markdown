---
layout: publication
title: Reasoning With Language Model Is Planning With World Model
authors: Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, Zhiting Hu
conference: "Arxiv"
year: 2023
bibkey: hao2023reasoning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.14992v2"}
tags: ['ARXIV']
---
Large language models (LLMs) have shown remarkable reasoning capabilities especially when prompted to generate intermediate reasoning steps (e.g. Chain-of-Thought CoT). However LLMs can still struggle with problems that are easy for humans such as generating action plans for executing tasks in a given environment or performing complex math logical and commonsense reasoning. The deficiency stems from the key fact that LLMs lack an internal () to predict the world () (e.g. environment status intermediate variable values) and simulate long-term outcomes of actions. This prevents LLMs from performing deliberate planning akin to human brains which involves exploring alternative reasoning paths anticipating future states and rewards and iteratively refining existing reasoning steps. To overcome the limitations we propose a new LLM reasoning framework ()easoning vi() ()lanning (). RAP repurposes the LLM as both a world model and a reasoning agent and incorporates a principled planning algorithm (based on Monto Carlo Tree Search) for strategic exploration in the vast reasoning space. During reasoning the LLM (as agent) incrementally builds a reasoning tree under the guidance of the LLM (as world model) and task-specific rewards and obtains a high-reward reasoning path efficiently with a proper balance between exploration () exploitation. We apply RAP to a variety of challenging reasoning problems including plan generation math reasoning and logical inference. Empirical results on these tasks demonstrate the superiority of RAP over various strong baselines including CoT and least-to-most prompting with self-consistency. RAP on LLAMA-33B surpasses CoT on GPT-4 with 3337; relative improvement in a plan generation setting.

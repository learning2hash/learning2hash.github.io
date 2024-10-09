---
layout: publication
title: Agentgym Evolving Large Language Model-based Agents Across Diverse Environments
authors: Zhiheng Xi, Yiwen Ding, Wenxiang Chen, Boyang Hong, Honglin Guo, Junzhe Wang, Dingwen Yang, Chenyang Liao, Xin Guo, Wei He, Songyang Gao, Lu Chen, Rui Zheng, Yicheng Zou, Tao Gui, Qi Zhang, Xipeng Qiu, Xuanjing Huang, Zuxuan Wu, Yu-gang Jiang
conference: "Arxiv"
year: 2024
bibkey: xi2024agentgym
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2406.04151v1"}
  - {name: "Code", url: "https://github.com/WooooDyy/AgentGym"}
tags: ['ARXIV', 'Has Code']
---
Building generalist agents that can handle diverse tasks and evolve themselves across different environments is a long-term goal in the AI community. Large language models (LLMs) are considered a promising foundation to build such agents due to their generalized capabilities. Current approaches either have LLM-based agents imitate expert-provided trajectories step-by-step requiring human supervision which is hard to scale and limits environmental exploration; or they let agents explore and learn in isolated environments resulting in specialist agents with limited generalization. In this paper we take the first step towards building generally-capable LLM-based agents with self-evolution ability. We identify a trinity of ingredients 1) diverse environments for agent exploration and learning 2) a trajectory set to equip agents with basic capabilities and prior knowledge and 3) an effective and scalable evolution method. We propose AgentGym a new framework featuring a variety of environments and tasks for broad real-time uni-format and concurrent agent exploration. AgentGym also includes a database with expanded instructions a benchmark suite and high-quality trajectories across environments. Next we propose a novel method AgentEvol to investigate the potential of agent self-evolution beyond previously seen data across tasks and environments. Experimental results show that the evolved agents can achieve results comparable to SOTA models. We release the AgentGym suite including the platform dataset benchmark checkpoints and algorithm implementations. The AgentGym suite is available on https://github.com/WooooDyy/AgentGym.

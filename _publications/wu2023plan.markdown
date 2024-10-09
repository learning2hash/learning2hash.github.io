---
layout: publication
title: Plan Eliminate And Track -- Language Models Are Good Teachers For Embodied Agents
authors: Yue Wu, So Yeon Min, Yonatan Bisk, Ruslan Salakhutdinov, Amos Azaria, Yuanzhi Li, Tom Mitchell, Shrimai Prabhumoye
conference: "Arxiv"
year: 2023
bibkey: wu2023plan
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.02412v2"}
tags: ['ARXIV']
---
Pre-trained large language models (LLMs) capture procedural knowledge about the world. Recent work has leveraged LLMs ability to generate abstract plans to simplify challenging control tasks either by action scoring or action modeling (fine-tuning). However the transformer architecture inherits several constraints that make it difficult for the LLM to directly serve as the agent e.g. limited input lengths fine-tuning inefficiency bias from pre-training and incompatibility with non-text environments. To maintain compatibility with a low-level trainable actor we propose to instead use the knowledge in LLMs to simplify the control problem rather than solving it. We propose the Plan Eliminate and Track (PET) framework. The Plan module translates a task description into a list of high-level sub-tasks. The Eliminate module masks out irrelevant objects and receptacles from the observation for the current sub-task. Finally the Track module determines whether the agent has accomplished each sub-task. On the AlfWorld instruction following benchmark the PET framework leads to a significant 1537; improvement over SOTA for generalization to human goal specifications.

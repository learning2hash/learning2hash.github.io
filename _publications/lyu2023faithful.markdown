---
layout: publication
title: Faithful Chain-of-thought Reasoning
authors: Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, Chris Callison-burch
conference: "Arxiv"
year: 2023
bibkey: lyu2023faithful
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2301.13379v3"}
tags: ['ARXIV']
---
While Chain-of-Thought (CoT) prompting boosts Language Models (LM) performance on a gamut of complex reasoning tasks the generated reasoning chain does not necessarily reflect how the model arrives at the answer (aka. faithfulness). We propose Faithful CoT a reasoning framework involving two stages Translation (Natural Language query (rightarrow) symbolic reasoning chain) and Problem Solving (reasoning chain (rightarrow) answer) using an LM and a deterministic solver respectively. This guarantees that the reasoning chain provides a faithful explanation of the final answer. Aside from interpretability Faithful CoT also improves empirical performance it outperforms standard CoT on 9 of 10 benchmarks from 4 diverse domains with a relative accuracy gain of 6.337; on Math Word Problems (MWP) 3.437; on Planning 5.537; on Multi-hop Question Answering (QA) and 21.437; on Relational Inference. Furthermore with GPT-4 and Codex it sets the new state-of-the-art few-shot performance on 7 datasets (with 95.0+ accuracy on 6 of them) showing a strong synergy between faithfulness and accuracy.

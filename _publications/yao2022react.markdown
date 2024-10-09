---
layout: publication
title: React Synergizing Reasoning And Acting In Language Models
authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
conference: "Arxiv"
year: 2022
bibkey: yao2022react
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.03629v3"}
  - {name: "Code", url: "https://react-lm.github.io"}
tags: ['ARXIV', 'Has Code']
---
While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner allowing for greater synergy between the two reasoning traces help the model induce track and update action plans as well as handle exceptions while actions allow it to interface with external sources such as knowledge bases or environments to gather additional information. We apply our approach named ReAct to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely on question answering (HotpotQA) and fact verification (Fever) ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop) ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 3437; and 1037; respectively while being prompted with only one or two in-context examples. Project site with code https://react-lm.github.io

---
layout: publication
title: Automatic Chain Of Thought Prompting In Large Language Models
authors: Zhuosheng Zhang, Aston Zhang, Mu Li, Alex Smola
conference: "Arxiv"
year: 2022
bibkey: zhang2022automatic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.03493v1"}
  - {name: "Code", url: "https://github.com/amazon-research/auto-cot"}
tags: ['ARXIV', 'Has Code']
---
Large language models (LLMs) can perform complex reasoning by generating intermediate reasoning steps. Providing these steps for prompting demonstrations is called chain-of-thought (CoT) prompting. CoT prompting has two major paradigms. One leverages a simple prompt like Lets think step by step to facilitate step-by-step thinking before answering a question. The other uses a few manual demonstrations one by one each composed of a question and a reasoning chain that leads to an answer. The superior performance of the second paradigm hinges on the hand-crafting of task-specific demonstrations one by one. We show that such manual efforts may be eliminated by leveraging LLMs with the Lets think step by step prompt to generate reasoning chains for demonstrations one by one i.e. lets think not just step by step but also one by one. However these generated chains often come with mistakes. To mitigate the effect of such mistakes we find that diversity matters for automatically constructing demonstrations. We propose an automatic CoT prompting method Auto-CoT. It samples questions with diversity and generates reasoning chains to construct demonstrations. On ten public benchmark reasoning tasks with GPT-3 Auto-CoT consistently matches or exceeds the performance of the CoT paradigm that requires manual designs of demonstrations. Code is available at https://github.com/amazon-research/auto-cot

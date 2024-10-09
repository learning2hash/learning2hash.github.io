---
layout: publication
title: RL4F Generating Natural Language Feedback With Reinforcement Learning For Repairing Model Outputs
authors: Afra Feyza Akyürek, Ekin Akyürek, Aman Madaan, Ashwin Kalyan, Peter Clark, Derry Wijaya, Niket Tandon
conference: "Arxiv"
year: 2023
bibkey: feyza2023generating
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.08844v2"}
tags: ['ARXIV']
---
Despite their unprecedented success even the largest language models make mistakes. Similar to how humans learn and improve using feedback previous work proposed providing language models with natural language feedback to guide them in repairing their outputs. Because human-generated critiques are expensive to obtain researchers have devised learned critique generators in lieu of human critics while assuming one can train downstream models to utilize generated feedback. However this approach does not apply to black-box or limited access models such as ChatGPT as they cannot be fine-tuned. Moreover in the era of large general-purpose language agents fine-tuning is neither computationally nor spatially efficient as it results in multiple copies of the network. In this work we introduce RL4F (Reinforcement Learning for Feedback) a multi-agent collaborative framework where the critique generator is trained to maximize end-task performance of GPT-3 a fixed model more than 200 times its size. RL4F produces critiques that help GPT-3 revise its outputs. We study three datasets for action planning summarization and alphabetization and show relative improvements up to 1037; in multiple text similarity metrics over other learned retrieval-augmented or prompting-based critique generators.

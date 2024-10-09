---
layout: publication
title: Program Of Thoughts Prompting Disentangling Computation From Reasoning For Numerical Reasoning Tasks
authors: Wenhu Chen, Xueguang Ma, Xinyi Wang, William W. Cohen
conference: "Arxiv"
year: 2022
bibkey: chen2022program
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2211.12588v4"}
  - {name: "Code", url: "https://github.com/wenhuchen/Program-of-Thoughts"}
tags: ['ARXIV', 'Has Code']
---
Recently there has been significant progress in teaching language models to perform step-by-step reasoning to solve complex numerical reasoning tasks. Chain-of-thoughts prompting (CoT) is by far the state-of-art method for these tasks. CoT uses language models to perform both reasoning and computation in the multi-step thought process. To disentangle computation from reasoning we propose Program of Thoughts (PoT) which uses language models (mainly Codex) to express the reasoning process as a program. The computation is relegated to an external computer which executes the generated programs to derive the answer. We evaluate PoT on five math word problem datasets (GSM AQuA SVAMP TabMWP MultiArith) and three financial-QA datasets (FinQA ConvFinQA TATQA) for both few-shot and zero-shot setups. Under both few-shot and zero-shot settings PoT can show an average performance gain over CoT by around 1237; across all the evaluated datasets. By combining PoT with self-consistency decoding we can achieve SoTA performance on all math problem datasets and near-SoTA performance on financial datasets. All of our data and code are released in Github https://github.com/wenhuchen/Program-of-Thoughts

---
layout: publication
title: Fine-tune Language Models To Approximate Unbiased In-context Learning
authors: Timothy Chu, Zhao Song, Chiwun Yang
conference: "Arxiv"
year: 2023
bibkey: chu2023fine
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2310.03331v1"}
tags: ['ARXIV']
---
In-context learning (ICL) is an astonishing emergent ability of large language models (LLMs). By presenting a prompt that includes multiple input-output pairs as examples and introducing a new query input models can generate the corresponding output. However the performance of models heavily relies on the quality of the input prompt when implementing in-context learning. Biased or imbalanced input prompts can significantly degrade the performance of language models. To address this issue we introduce a reweighted algorithm called RICL (Reweighted In-context Learning). This algorithm fine-tunes language models using an unbiased validation set to determine the optimal weight for each input-output example to approximate unbiased in-context learning. Furthermore we also introduce a low-cost reweighted algorithm a linear optimal weight approximation algorithm called LARICL (Linear Approximation of Reweighted In-context Learning). This algorithm requires minimal training cost while providing effective results. We prove the convergence of our algorithm and validate its performance through experiments conducted on a numerical dataset. The experimental findings reveal a substantial improvement in comparison to benchmarks including the performance of casual prompt-based in-context learning and the performance of a classic fine-tuning method.

---
layout: publication
title: An Empirical Analysis Of Compute-optimal Inference For Problem-solving With Language Models
authors: Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang
conference: "Arxiv"
year: 2024
bibkey: wu2024empirical
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2408.00724v1"}
tags: ['ARXIV']
---
The optimal training configurations of large language models (LLMs) with respect to model sizes and compute budgets have been extensively studied. But how to optimally configure LLMs during inference has not been explored in sufficient depth. We study compute-optimal inference designing models and inference strategies that optimally trade off additional inference-time compute for improved performance. As a first step towards understanding and designing compute-optimal inference methods we assessed the effectiveness and computational efficiency of multiple inference strategies such as Greedy Search Majority Voting Best-of-N Weighted Voting and their variants on two different Tree Search algorithms involving different model sizes and computational budgets. We found that a smaller language model with a novel tree search algorithm typically achieves a Pareto-optimal trade-off. These results highlight the potential benefits of deploying smaller models equipped with more sophisticated decoding algorithms in budget-constrained scenarios e.g. on end-devices to enhance problem-solving accuracy. For instance we show that the Llemma-7B model can achieve competitive accuracy to a Llemma-34B model on MATH500 while using (2times) less FLOPs. Our findings could potentially apply to any generation task with a well-defined measure of success.

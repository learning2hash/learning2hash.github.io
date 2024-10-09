---
layout: publication
title: Large Language Models Are Versatile Decomposers Decompose Evidence And Questions For Table-based Reasoning
authors: Yunhu Ye, Binyuan Hui, Min Yang, Binhua Li, Fei Huang, Yongbin Li
conference: "Arxiv"
year: 2023
bibkey: ye2023large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2301.13808v3"}
tags: ['ARXIV']
---
Table-based reasoning has shown remarkable progress in combining deep models with discrete reasoning which requires reasoning over both free-form natural language (NL) questions and structured tabular data. However previous table-based reasoning solutions usually suffer from significant performance degradation on huge evidence (tables). In addition most existing methods struggle to reason over complex questions since the required information is scattered in different places. To alleviate the above challenges we exploit large language models (LLMs) as decomposers for effective table-based reasoning which (i) decompose huge evidence (a huge table) into sub-evidence (a small table) to mitigate the interference of useless information for table reasoning; and (ii) decompose complex questions into simpler sub-questions for text reasoning. Specifically we first use the LLMs to break down the evidence (tables) involved in the current question retaining the relevant evidence and excluding the remaining irrelevant evidence from the huge table. In addition we propose a parsing-execution-filling strategy to alleviate the hallucination dilemma of the chain of thought by decoupling logic and numerical computation in each step. Extensive experiments show that our method can effectively leverage decomposed evidence and questions and outperforms the strong baselines on TabFact WikiTableQuestion and FetaQA datasets. Notably our model outperforms human performance for the first time on the TabFact dataset.

---
layout: publication
title: Chatdb Augmenting Llms With Databases As Their Symbolic Memory
authors: Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo, Junbo Zhao, Hang Zhao
conference: "Arxiv"
year: 2023
bibkey: hu2023chatdb
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2306.03901v2"}
tags: ['ARXIV']
---
Large language models (LLMs) with memory are computationally universal. However mainstream LLMs are not taking full advantage of memory and the designs are heavily influenced by biological brains. Due to their approximate nature and proneness to the accumulation of errors conventional neural memory mechanisms cannot support LLMs to simulate complex reasoning. In this paper we seek inspiration from modern computer architectures to augment LLMs with symbolic memory for complex multi-hop reasoning. Such a symbolic memory framework is instantiated as an LLM and a set of SQL databases where the LLM generates SQL instructions to manipulate the SQL databases. We validate the effectiveness of the proposed memory framework on a synthetic dataset requiring complex reasoning. The project website is available at https://chatdatabase.github.io/ .

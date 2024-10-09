---
layout: publication
title: Large Language Model With Graph Convolution For Recommendation
authors: Yingpeng Du, Ziyan Wang, Zhu Sun, Haoyan Chua, Hongzhi Liu, Zhonghai Wu, Yining Ma, Jie Zhang, Youchen Sun
conference: "Arxiv"
year: 2024
bibkey: du2024large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.08859v1"}
tags: ['ARXIV', 'Graph']
---
In recent years efforts have been made to use text information for better user profiling and item characterization in recommendations. However text information can sometimes be of low quality hindering its effectiveness for real-world applications. With knowledge and reasoning capabilities capsuled in Large Language Models (LLMs) utilizing LLMs emerges as a promising way for description improvement. However existing ways of prompting LLMs with raw texts ignore structured knowledge of user-item interactions which may lead to hallucination problems like inconsistent description generation. To this end we propose a Graph-aware Convolutional LLM method to elicit LLMs to capture high-order relations in the user-item graph. To adapt text-based LLMs with structured graphs We use the LLM as an aggregator in graph processing allowing it to understand graph-based information step by step. Specifically the LLM is required for description enhancement by exploring multi-hop neighbors layer by layer thereby propagating information progressively in the graph. To enable LLMs to capture large-scale graph information we break down the description task into smaller parts which drastically reduces the context length of the token input with each step. Extensive experiments on three real-world datasets show that our method consistently outperforms state-of-the-art methods.

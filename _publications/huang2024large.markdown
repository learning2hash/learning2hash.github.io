---
layout: publication
title: Large Language Model Interaction Simulator For Cold-start Item Recommendation
authors: Feiran Huang, Zhenghang Yang, Junyi Jiang, Yuanchen Bei, Yijie Zhang, Hao Chen
conference: "Arxiv"
year: 2024
bibkey: huang2024large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.09176v1"}
tags: ['ARXIV']
---
Recommending cold items is a long-standing challenge for collaborative filtering models because these cold items lack historical user interactions to model their collaborative features. The gap between the content of cold items and their behavior patterns makes it difficult to generate accurate behavioral embeddings for cold items. Existing cold-start models use mapping functions to generate fake behavioral embeddings based on the content feature of cold items. However these generated embeddings have significant differences from the real behavioral embeddings leading to a negative impact on cold recommendation performance. To address this challenge we propose an LLM Interaction Simulator (LLM-InS) to model users behavior patterns based on the content aspect. This simulator allows recommender systems to simulate vivid interactions for each cold item and transform them from cold to warm items directly. Specifically we outline the designing and training process of a tailored LLM-simulator that can simulate the behavioral patterns of users and items. Additionally we introduce an efficient filtering-and-refining approach to take full advantage of the simulation power of the LLMs. Finally we propose an updating method to update the embeddings of the items. we unified trains for both cold and warm items within a recommender model based on the simulated and real interactions. Extensive experiments using real behavioral embeddings demonstrate that our proposed model LLM-InS outperforms nine state-of-the-art cold-start methods and three LLM models in cold-start item recommendations.

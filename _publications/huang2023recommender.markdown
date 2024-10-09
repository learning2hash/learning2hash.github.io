---
layout: publication
title: Recommender AI Agent Integrating Large Language Models For Interactive Recommendations
authors: Xu Huang, Jianxun Lian, Yuxuan Lei, Jing Yao, Defu Lian, Xing Xie
conference: "Arxiv"
year: 2023
bibkey: huang2023recommender
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2308.16505v3"}
  - {name: "Code", url: "https://aka.ms/recagent"}
tags: ['ARXIV', 'Has Code']
---
Recommender models excel at providing domain-specific item recommendations by leveraging extensive user behavior data. Despite their ability to act as lightweight domain experts they struggle to perform versatile tasks such as providing explanations and engaging in conversations. On the other hand large language models (LLMs) represent a significant step towards artificial general intelligence showcasing remarkable capabilities in instruction comprehension commonsense reasoning and human interaction. However LLMs lack the knowledge of domain-specific item catalogs and behavioral patterns particularly in areas that diverge from general world knowledge such as online e-commerce. Finetuning LLMs for each domain is neither economic nor efficient. In this paper we bridge the gap between recommender models and LLMs combining their respective strengths to create a versatile and interactive recommender system. We introduce an efficient framework called textbfInteRecAgent which employs LLMs as the brain and recommender models as tools. We first outline a minimal set of essential tools required to transform LLMs into InteRecAgent. We then propose an efficient workflow within InteRecAgent for task execution incorporating key components such as memory components dynamic demonstration-augmented task planning and reflection. InteRecAgent enables traditional recommender systems such as those ID-based matrix factorization models to become interactive systems with a natural language interface through the integration of LLMs. Experimental results on several public datasets show that InteRecAgent achieves satisfying performance as a conversational recommender system outperforming general-purpose LLMs. The source code of InteRecAgent is released at https://aka.ms/recagent.

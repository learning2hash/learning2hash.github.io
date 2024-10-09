---
layout: publication
title: Recommendation As Instruction Following A Large Language Model Empowered Recommendation Approach
authors: Junjie Zhang, Ruobing Xie, Yupeng Hou, Wayne Xin Zhao, Leyu Lin, Ji-rong Wen
conference: "Arxiv"
year: 2023
bibkey: zhang2023recommendation
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.07001v1"}
tags: ['ARXIV']
---
In the past decades recommender systems have attracted much attention in both research and industry communities and a large number of studies have been devoted to developing effective recommendation models. Basically speaking these models mainly learn the underlying user preference from historical behavior data and then estimate the user-item matching relationships for recommendations. Inspired by the recent progress on large language models (LLMs) we take a different approach to developing the recommendation models considering recommendation as instruction following by LLMs. The key idea is that the preferences or needs of a user can be expressed in natural language descriptions (called instructions) so that LLMs can understand and further execute the instruction for fulfilling the recommendation task. Instead of using public APIs of LLMs we instruction tune an open-source LLM (3B Flan-T5-XL) in order to better adapt LLMs to recommender systems. For this purpose we first design a general instruction format for describing the preference intention task form and context of a user in natural language. Then we manually design 39 instruction templates and automatically generate a large amount of user-personalized instruction data (252K instructions) with varying types of preferences and intentions. To demonstrate the effectiveness of our approach we instantiate the instruction templates into several widely-studied recommendation (or search) tasks and conduct extensive experiments on these tasks with real-world datasets. Experiment results show that the proposed approach can outperform several competitive baselines including the powerful GPT-3.5 on these evaluation tasks. Our approach sheds light on developing more user-friendly recommender systems in which users can freely communicate with the system and obtain more accurate recommendations via natural language instructions.

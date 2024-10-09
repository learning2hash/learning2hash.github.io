---
layout: publication
title: Llara Large Language-recommendation Assistant
authors: Jiayi Liao, Sihang Li, Zhengyi Yang, Jiancan Wu, Yancheng Yuan, Xiang Wang, Xiangnan He
conference: "Arxiv"
year: 2023
bibkey: liao2023llara
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2312.02445v4"}
  - {name: "Code", url: "https://github.com/ljy0ustc/LLaRA"}
tags: ['ARXIV', 'Has Code']
---
Sequential recommendation aims to predict users next interaction with items based on their past engagement sequence. Recently the advent of Large Language Models (LLMs) has sparked interest in leveraging them for sequential recommendation viewing it as language modeling. Previous studies represent items within LLMs input prompts as either ID indices or textual metadata. However these approaches often fail to either encapsulate comprehensive world knowledge or exhibit sufficient behavioral understanding. To combine the complementary strengths of conventional recommenders in capturing behavioral patterns of users and LLMs in encoding world knowledge about items we introduce Large Language-Recommendation Assistant (LLaRA). Specifically it uses a novel hybrid prompting method that integrates ID-based item embeddings learned by traditional recommendation models with textual item features. Treating the sequential behaviors of users as a distinct modality beyond texts we employ a projector to align the traditional recommenders ID embeddings with the LLMs input space. Moreover rather than directly exposing the hybrid prompt to LLMs a curriculum learning strategy is adopted to gradually ramp up training complexity. Initially we warm up the LLM using text-only prompts which better suit its inherent language modeling ability. Subsequently we progressively transition to the hybrid prompts training the model to seamlessly incorporate the behavioral knowledge from the traditional sequential recommender into the LLM. Empirical results validate the effectiveness of our proposed framework. Codes are available at https://github.com/ljy0ustc/LLaRA.

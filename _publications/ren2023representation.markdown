---
layout: publication
title: Representation Learning With Large Language Models For Recommendation
authors: Xubin Ren, Wei Wei, Lianghao Xia, Lixin Su, Suqi Cheng, Junfeng Wang, Dawei Yin, Chao Huang
conference: "Arxiv"
year: 2023
bibkey: ren2023representation
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2310.15950v4"}
  - {name: "Code", url: "https://github.com/HKUDS/RLMRec"}
tags: ['ARXIV', 'Cross Modal', 'Deep Learning', 'Graph', 'Has Code', 'Supervised']
---
Recommender systems have seen significant advancements with the influence of deep learning and graph neural networks particularly in capturing complex user-item relationships. However these graph-based recommenders heavily depend on ID-based data potentially disregarding valuable textual information associated with users and items resulting in less informative learned representations. Moreover the utilization of implicit feedback data introduces potential noise and bias posing challenges for the effectiveness of user preference learning. While the integration of large language models (LLMs) into traditional ID-based recommenders has gained attention challenges such as scalability issues limitations in text-only reliance and prompt input constraints need to be addressed for effective implementation in practical recommender systems. To address these challenges we propose a model-agnostic framework RLMRec that aims to enhance existing recommenders with LLM-empowered representation learning. It proposes a recommendation paradigm that integrates representation learning with LLMs to capture intricate semantic aspects of user behaviors and preferences. RLMRec incorporates auxiliary textual signals develops a user/item profiling paradigm empowered by LLMs and aligns the semantic space of LLMs with the representation space of collaborative relational signals through a cross-view alignment framework. This work further establish a theoretical foundation demonstrating that incorporating textual signals through mutual information maximization enhances the quality of representations. In our evaluation we integrate RLMRec with state-of-the-art recommender models while also analyzing its efficiency and robustness to noise data. Our implementation codes are available at https://github.com/HKUDS/RLMRec.

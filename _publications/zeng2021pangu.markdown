---
layout: publication
title: Pangu-(α) Large-scale Autoregressive Pretrained Chinese Language Models With Auto-parallel Computation
authors: Wei Zeng, Xiaozhe Ren, Teng Su, Hui Wang, Yi Liao, Zhiwei Wang, Xin Jiang, Zhenzhang Yang, Kaisheng Wang, Xiaoda Zhang, Chen Li, Ziyan Gong, Yifan Yao, Xinjing Huang, Jun Wang, Jianfeng Yu, Qi Guo, Yue Yu, Yan Zhang, Jin Wang, Hengtao Tao, Dasen Yan, Zexuan Yi, Fang Peng, Fangqing Jiang, Han Zhang, Lingfeng Deng, Yehong Zhang, Zhe Lin, Chao Zhang, Shaojie Zhang, Mingyue Guo, Shanzhi Gu, Gaojun Fan, Yaowei Wang, Xuefeng Jin, Qun Liu, Yonghong Tian
conference: "Arxiv"
year: 2021
bibkey: zeng2021pangu
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2104.12369v1"}
tags: ['ARXIV']
---
Large-scale Pretrained Language Models (PLMs) have become the new paradigm for Natural Language Processing (NLP). PLMs with hundreds of billions parameters such as GPT-3 have demonstrated strong performances on natural language understanding and generation with textitfew-shot in-context learning. In this work we present our practice on training large-scale autoregressive language models named PanGu-(alpha) with up to 200 billion parameters. PanGu-(alpha) is developed under the MindSpore and trained on a cluster of 2048 Ascend 910 AI processors. The training parallelism strategy is implemented based on MindSpore Auto-parallel which composes five parallelism dimensions to scale the training task to 2048 processors efficiently including data parallelism op-level model parallelism pipeline model parallelism optimizer model parallelism and rematerialization. To enhance the generalization ability of PanGu-(alpha) we collect 1.1TB high-quality Chinese data from a wide range of domains to pretrain the model. We empirically test the generation ability of PanGu-(alpha) in various scenarios including text summarization question answering dialogue generation etc. Moreover we investigate the effect of model scales on the few-shot performances across a broad range of Chinese NLP tasks. The experimental results demonstrate the superior capabilities of PanGu-(alpha) in performing various tasks under few-shot or zero-shot settings.

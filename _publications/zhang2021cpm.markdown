---
layout: publication
title: CPM-2 Large-scale Cost-effective Pre-trained Language Models
authors: Zhengyan Zhang, Yuxian Gu, Xu Han, Shengqi Chen, Chaojun Xiao, Zhenbo Sun, Yuan Yao, Fanchao Qi, Jian Guan, Pei Ke, Yanzheng Cai, Guoyang Zeng, Zhixing Tan, Zhiyuan Liu, Minlie Huang, Wentao Han, Yang Liu, Xiaoyan Zhu, Maosong Sun
conference: "Arxiv"
year: 2021
bibkey: zhang2021cpm
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2106.10715v3"}
  - {name: "Code", url: "https://github.com/TsinghuaAI/CPM"}
tags: ['ARXIV', 'Has Code']
---
In recent years the size of pre-trained language models (PLMs) has grown by leaps and bounds. However efficiency issues of these large-scale PLMs limit their utilization in real-world scenarios. We present a suite of cost-effective techniques for the use of PLMs to deal with the efficiency issues of pre-training fine-tuning and inference. (1) We introduce knowledge inheritance to accelerate the pre-training process by exploiting existing PLMs instead of training models from scratch. (2) We explore the best practice of prompt tuning with large-scale PLMs. Compared with conventional fine-tuning prompt tuning significantly reduces the number of task-specific parameters. (3) We implement a new inference toolkit namely InfMoE for using large-scale PLMs with limited computational resources. Based on our cost-effective pipeline we pre-train two models an encoder-decoder bilingual model with 11 billion parameters (CPM-2) and its corresponding MoE version with 198 billion parameters. In our experiments we compare CPM-2 with mT5 on downstream tasks. Experimental results show that CPM-2 has excellent general language intelligence. Moreover we validate the efficiency of InfMoE when conducting inference of large-scale models having tens of billions of parameters on a single GPU. All source code and model parameters are available at https://github.com/TsinghuaAI/CPM.

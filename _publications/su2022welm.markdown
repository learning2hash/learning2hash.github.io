---
layout: publication
title: Welm A Well-read Pre-trained Language Model For Chinese
authors: Hui Su, Xiao Zhou, Houjin Yu, Xiaoyu Shen, Yuwen Chen, Zilin Zhu, Yang Yu, Jie Zhou
conference: "Arxiv"
year: 2022
bibkey: su2022welm
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2209.10372v5"}
  - {name: "Code", url: "https://welm.weixin.qq.com/docs/api/"}
tags: ['ARXIV', 'Has Code', 'Unsupervised']
---
Large Language Models pre-trained with self-supervised learning have demonstrated impressive zero-shot generalization capabilities on a wide spectrum of tasks. In this work we present WeLM a well-read pre-trained language model for Chinese that is able to seamlessly perform different types of tasks with zero or few-shot demonstrations. WeLM is trained with 10B parameters by reading a curated high-quality corpus covering a wide range of topics. We show that WeLM is equipped with broad knowledge on various domains and languages. On 18 monolingual (Chinese) tasks WeLM can significantly outperform existing pre-trained models with similar sizes and match the performance of models up to 25 times larger. WeLM also exhibits strong capabilities in multi-lingual and code-switching understanding outperforming existing multilingual language models pre-trained on 30 languages. Furthermore We collected human-written prompts for a large set of supervised datasets in Chinese and fine-tuned WeLM with multi-prompted training. The resulting model can attain strong generalization on unseen types of tasks and outperform the unsupervised WeLM in zero-shot learning. Finally we demonstrate that WeLM has basic skills at explaining and calibrating the decisions from itself which can be promising directions for future research. Our models can be applied from https://welm.weixin.qq.com/docs/api/.

---
layout: publication
title: Pre-training Tasks for User Intent Detection and Embedding Retrieval in E-commerce
  Search
authors: Qiu Yiming, Zhao Chenyu, Zhang Han, Zhuo Jingwei, Li Tianhao, Zhang Xiaowei,
  Wang Songlin, Xu Sulong, Long Bo, Yang Wen-yun
conference: Proceedings of the 31st ACM International Conference on Information &amp;
  Knowledge Management
year: 2022
bibkey: qiu2022pre
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.06150'}]
tags: ["Datasets", "CIKM"]
short_authors: Qiu et al.
---
BERT-style models pre-trained on the general corpus (e.g., Wikipedia) and
fine-tuned on specific task corpus, have recently emerged as breakthrough
techniques in many NLP tasks: question answering, text classification, sequence
labeling and so on. However, this technique may not always work, especially for
two scenarios: a corpus that contains very different text from the general
corpus Wikipedia, or a task that learns embedding spacial distribution for a
specific purpose (e.g., approximate nearest neighbor search). In this paper, to
tackle the above two scenarios that we have encountered in an industrial
e-commerce search system, we propose customized and novel pre-training tasks
for two critical modules: user intent detection and semantic embedding
retrieval. The customized pre-trained models after fine-tuning, being less than
10% of BERT-base's size in order to be feasible for cost-efficient CPU serving,
significantly improve the other baseline models: 1) no pre-training model and
2) fine-tuned model from the official pre-trained BERT using general corpus, on
both offline datasets and online system. We have open sourced our datasets for
the sake of reproducibility and future works.
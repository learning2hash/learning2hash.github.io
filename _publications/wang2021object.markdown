---
layout: publication
title: Object-aware Video-language Pre-training For Retrieval
authors: Alex Jinpeng Wang, Yixiao Ge, Guanyu Cai, Rui Yan, Xudong Lin, Ying Shan,
  Xiaohu Qie, Mike Zheng Shou
conference: Arxiv
year: 2021
bibkey: wang2021object
citations: 0
additional_links: [{name: Code, url: 'https://github.com/FingerRec/OA-Transformer'},
  {name: Paper, url: 'https://arxiv.org/abs/2112.00656'}]
tags: [Scalability, Evaluation, Datasets]
short_authors: Wang et al.
---
Recently, by introducing large-scale dataset and strong transformer network,
video-language pre-training has shown great success especially for retrieval.
Yet, existing video-language transformer models do not explicitly fine-grained
semantic align. In this work, we present Object-aware Transformers, an
object-centric approach that extends video-language transformer to incorporate
object representations. The key idea is to leverage the bounding boxes and
object tags to guide the training process. We evaluate our model on three
standard sub-tasks of video-text matching on four widely used benchmarks. We
also provide deep analysis and detailed ablation about the proposed method. We
show clear improvement in performance across all tasks and datasets considered,
demonstrating the value of a model that incorporates object representations
into a video-language architecture. The code will be released at
https://github.com/FingerRec/OA-Transformer.
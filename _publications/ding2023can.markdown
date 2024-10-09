---
layout: publication
title: Gpt4image Can Large Pre-trained Models Help Vision Models On Perception Tasks
authors: Ning Ding, Yehui Tang, Zhongqian Fu, Chao Xu, Kai Han, Yunhe Wang
conference: "Arxiv"
year: 2023
bibkey: ding2023can
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2306.00693v2"}
tags: ['ARXIV', 'CNN', 'Cross Modal', 'Deep Learning', 'Supervised']
---
The recent upsurge in pre-trained large models (e.g. GPT-4) has swept across the entire deep learning community. Such powerful large language models (LLMs) demonstrate advanced generative ability and multimodal understanding capability which quickly achieve new state-of-the-art performances on a variety of benchmarks. The pre-trained LLM usually plays the role as a universal AI model that can conduct various tasks including context reasoning article analysis and image content comprehension. However considering the prohibitively high memory and computational cost for implementing such a large model the conventional models (such as CNN and ViT) are still essential for many visual perception tasks. In this paper we propose to enhance the representation ability of ordinary vision models for perception tasks (e.g. image classification) by taking advantage of large pre-trained models. We present a new learning paradigm in which the knowledge extracted from large pre-trained models are utilized to help models like CNN and ViT learn enhanced representations and achieve better performance. Firstly we curate a high quality description set by prompting a multimodal LLM to generate descriptive text for all training images. Furthermore we feed these detailed descriptions into a pre-trained encoder to extract text embeddings with rich semantic information that encodes the content of images. During training text embeddings will serve as extra supervising signals and be aligned with image representations learned by vision models. The alignment process helps vision models learn better and achieve higher accuracy with the assistance of pre-trained LLMs. We conduct extensive experiments to verify that the proposed algorithm consistently improves the performance for various vision models with heterogeneous architectures.

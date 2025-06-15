---
layout: publication
title: 'IDMR: Towards Instance-driven Precise Visual Correspondence In Multimodal Retrieval'
authors: Bangwei Liu et al.
conference: "Arxiv"
year: 2025
citations: 0
bibkey: liu2025towards
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2504.00954'}
  - {name: "Code", url: 'https://github.com/BwLiu01/IDMR'}
tags: ['Tools and Libraries', 'Evaluation Metrics', 'Has Code', 'Applications']
---
Multimodal retrieval systems are becoming increasingly vital for cutting-edge
AI technologies, such as embodied AI and AI-driven digital content industries.
However, current multimodal retrieval tasks lack sufficient complexity and
demonstrate limited practical application value. It spires us to design
Instance-Driven Multimodal Image Retrieval (IDMR), a novel task that requires
models to retrieve images containing the same instance as a query image while
matching a text-described scenario. Unlike existing retrieval tasks focused on
global image similarity or category-level matching, IDMR demands fine-grained
instance-level consistency across diverse contexts. To benchmark this
capability, we develop IDMR-bench using real-world object tracking and
first-person video data. Addressing the scarcity of training data, we propose a
cross-domain synthesis method that creates 557K training samples by cropping
objects from standard detection datasets. Our Multimodal Large Language Model
(MLLM) based retrieval model, trained on 1.2M samples, outperforms
state-of-the-art approaches on both traditional benchmarks and our zero-shot
IDMR-bench. Experimental results demonstrate previous models' limitations in
instance-aware retrieval and highlight the potential of MLLM for advanced
retrieval applications. The whole training dataset, codes and models, with wide
ranges of sizes, are available at https://github.com/BwLiu01/IDMR.

---
layout: publication
title: Detecting And Mitigating Hallucination In Large Vision Language Models Via Fine-grained AI Feedback
authors: Wenyi Xiao, Ziwei Huang, Leilei Gan, Wanggui He, Haoyuan Li, Zhelun Yu, Hao Jiang, Fei Wu, Linchao Zhu
conference: "Arxiv"
year: 2024
bibkey: xiao2024detecting
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2404.14233v1"}
tags: ['ARXIV']
---
The rapidly developing Large Vision Language Models (LVLMs) have shown notable capabilities on a range of multi-modal tasks but still face the hallucination phenomena where the generated texts do not align with the given contexts significantly restricting the usages of LVLMs. Most previous work detects and mitigates hallucination at the coarse-grained level or requires expensive annotation (e.g. labeling by proprietary models or human experts). To address these issues we propose detecting and mitigating hallucinations in LVLMs via fine-grained AI feedback. The basic idea is that we generate a small-size sentence-level hallucination annotation dataset by proprietary models whereby we train a hallucination detection model which can perform sentence-level hallucination detection covering primary hallucination types (i.e. object attribute and relationship). Then we propose a detect-then-rewrite pipeline to automatically construct preference dataset for training hallucination mitigating model. Furthermore we propose differentiating the severity of hallucinations and introducing a Hallucination Severity-Aware Direct Preference Optimization (HSA-DPO) for mitigating hallucination in LVLMs by incorporating the severity of hallucinations into preference learning. Extensive experiments demonstrate the effectiveness of our method.

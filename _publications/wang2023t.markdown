---
layout: publication
title: T-sciq Teaching Multimodal Chain-of-thought Reasoning Via Mixed Large Language Model Signals For Science Question Answering
authors: Lei Wang, Yi Hu, Jiabang He, Xing Xu, Ning Liu, Hui Liu, Heng Tao Shen
conference: "Arxiv"
year: 2023
bibkey: wang2023t
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.03453v4"}
  - {name: "Code", url: "https://github.com/T-SciQ/T-SciQ"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
Large Language Models (LLMs) have recently demonstrated exceptional performance in various Natural Language Processing (NLP) tasks. They have also shown the ability to perform chain-of-thought (CoT) reasoning to solve complex problems. Recent studies have explored CoT reasoning in complex multimodal scenarios such as the science question answering task by fine-tuning multimodal models with high-quality human-annotated CoT rationales. However collecting high-quality COT rationales is usually time-consuming and costly. Besides the annotated rationales are hardly accurate due to the external essential information missed. To address these issues we propose a novel method termed T-SciQ that aims at teaching science question answering with LLM signals. The T-SciQ approach generates high-quality CoT rationales as teaching signals and is advanced to train much smaller models to perform CoT reasoning in complex modalities. Additionally we introduce a novel data mixing strategy to produce more effective teaching data samples for simple and complex science question answer problems. Extensive experimental results show that our T-SciQ method achieves a new state-of-the-art performance on the ScienceQA benchmark with an accuracy of 96.1837;. Moreover our approach outperforms the most powerful fine-tuned baseline by 4.537;. The code is publicly available at https://github.com/T-SciQ/T-SciQ.

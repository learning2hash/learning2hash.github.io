---
layout: publication
title: 'Camel: Cross-modality Adaptive Meta-learning For Text-based Person Retrieval'
authors: Hang Yu, Jiahao Wen, Zhedong Zheng
conference: IEEE Transactions on Information Forensics and Security
year: 2025
bibkey: yu2025camel
citations: 1
additional_links: [{name: Code, url: 'https://github.com/Jahawn-Wen/CAMeL-reID'},
  {name: Paper, url: 'https://arxiv.org/abs/2504.18782'}]
tags: ["Privacy & Security", "Robustness", "Scalability", "Tools & Libraries"]
short_authors: Hang Yu, Jiahao Wen, Zhedong Zheng
---
Text-based person retrieval aims to identify specific individuals within an
image database using textual descriptions. Due to the high cost of annotation
and privacy protection, researchers resort to synthesized data for the paradigm
of pretraining and fine-tuning. However, these generated data often exhibit
domain biases in both images and textual annotations, which largely compromise
the scalability of the pre-trained model. Therefore, we introduce a
domain-agnostic pretraining framework based on Cross-modality Adaptive
Meta-Learning (CAMeL) to enhance the model generalization capability during
pretraining to facilitate the subsequent downstream tasks. In particular, we
develop a series of tasks that reflect the diversity and complexity of
real-world scenarios, and introduce a dynamic error sample memory unit to
memorize the history for errors encountered within multiple tasks. To further
ensure multi-task adaptation, we also adopt an adaptive dual-speed update
strategy, balancing fast adaptation to new tasks and slow weight updates for
historical tasks. Albeit simple, our proposed model not only surpasses existing
state-of-the-art methods on real-world benchmarks, including CUHK-PEDES,
ICFG-PEDES, and RSTPReid, but also showcases robustness and scalability in
handling biased synthetic images and noisy text annotations. Our code is
available at https://github.com/Jahawn-Wen/CAMeL-reID.
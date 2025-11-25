---
layout: publication
title: Transformer-based Cross-modal Recipe Embeddings With Large Batch Training
authors: Jing Yang, Junwen Chen, Keiji Yanai
conference: Lecture Notes in Computer Science
year: 2022
bibkey: yang2022transformer
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.04948'}]
tags: ["Multimodal Retrieval", "Self-Supervised"]
short_authors: Jing Yang, Junwen Chen, Keiji Yanai
---
In this paper, we present a cross-modal recipe retrieval framework,
Transformer-based Network for Large Batch Training (TNLBT), which is inspired
by ACME~(Adversarial Cross-Modal Embedding) and H-T~(Hierarchical Transformer).
TNLBT aims to accomplish retrieval tasks while generating images from recipe
embeddings. We apply the Hierarchical Transformer-based recipe text encoder,
the Vision Transformer~(ViT)-based recipe image encoder, and an adversarial
network architecture to enable better cross-modal embedding learning for recipe
texts and images. In addition, we use self-supervised learning to exploit the
rich information in the recipe texts having no corresponding images. Since
contrastive learning could benefit from a larger batch size according to the
recent literature on self-supervised learning, we adopt a large batch size
during training and have validated its effectiveness. In the experiments, the
proposed framework significantly outperformed the current state-of-the-art
frameworks in both cross-modal recipe retrieval and image generation tasks on
the benchmark Recipe1M. This is the first work which confirmed the
effectiveness of large batch training on cross-modal recipe embeddings.
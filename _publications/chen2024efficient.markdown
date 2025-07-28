---
layout: publication
title: 'Efficient Ternary Weight Embedding Model: Bridging Scalability And Performance'
authors: Jiayi Chen, Chen Wu, Shaoqun Zhang, Nan Li, Liangjie Zhang, Qi Zhang
conference: Arxiv
year: 2024
bibkey: chen2024efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.15438'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Chen et al.
---
Embedding models have become essential tools in both natural language
processing and computer vision, enabling efficient semantic search,
recommendation, clustering, and more. However, the high memory and
computational demands of full-precision embeddings pose challenges for
deployment in resource-constrained environments, such as real-time
recommendation systems. In this work, we propose a novel finetuning framework
to ternary-weight embedding models, which reduces memory and computational
overhead while maintaining high performance. To apply ternarization to
pre-trained embedding models, we introduce self-taught knowledge distillation
to finalize the ternary-weights of the linear layers. With extensive
experiments on public text and vision datasets, we demonstrated that without
sacrificing effectiveness, the ternarized model consumes low memory usage and
has low latency in the inference stage with great efficiency. In practical
implementations, embedding models are typically integrated with Approximate
Nearest Neighbor (ANN) search. Our experiments combining ternary embedding with
ANN search yielded impressive improvement in both accuracy and computational
efficiency. The repository is available at here.
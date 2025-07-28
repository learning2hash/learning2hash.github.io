---
layout: publication
title: Class-relevant Patch Embedding Selection For Few-shot Image Classification
authors: Weihao Jiang, Haoyang Cui, Kun He
conference: Arxiv
year: 2025
bibkey: jiang2024class
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.03722'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Weihao Jiang, Haoyang Cui, Kun He
---
Effective image classification hinges on discerning relevant features from
both foreground and background elements, with the foreground typically holding
the critical information. While humans adeptly classify images with limited
exposure, artificial neural networks often struggle with feature selection from
rare samples. To address this challenge, we propose a novel method for
selecting class-relevant patch embeddings. Our approach involves splitting
support and query images into patches, encoding them using a pre-trained Vision
Transformer (ViT) to obtain class embeddings and patch embeddings,
respectively. Subsequently, we filter patch embeddings using class embeddings
to retain only the class-relevant ones. For each image, we calculate the
similarity between class embedding and each patch embedding, sort the
similarity sequence in descending order, and only retain top-ranked patch
embeddings. By prioritizing similarity between the class embedding and patch
embeddings, we select top-ranked patch embeddings to be fused with class
embedding to form a comprehensive image representation, enhancing pattern
recognition across instances. Our strategy effectively mitigates the impact of
class-irrelevant patch embeddings, yielding improved performance in pre-trained
models. Extensive experiments on popular few-shot classification benchmarks
demonstrate the simplicity, efficacy, and computational efficiency of our
approach, outperforming state-of-the-art baselines under both 5-shot and 1-shot
scenarios.
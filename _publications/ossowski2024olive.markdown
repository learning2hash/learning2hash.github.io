---
layout: publication
title: 'OLIVE: Object Level In-context Visual Embeddings'
authors: Timothy Ossowski, Junjie Hu
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: ossowski2024olive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.00872'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Robustness"]
short_authors: Timothy Ossowski, Junjie Hu
---
Recent generalist vision-language models (VLMs) have demonstrated impressive
reasoning capabilities across diverse multimodal tasks. However, these models
still struggle with fine-grained object-level understanding and grounding. In
terms of modeling, existing VLMs implicitly align text tokens with image patch
tokens, which is ineffective for embedding alignment at the same granularity
and inevitably introduces noisy spurious background features. Additionally,
these models struggle when generalizing to unseen visual concepts and may not
be reliable for domain-specific tasks without further fine-tuning. To address
these limitations, we propose a novel method to prompt large language models
with in-context visual object vectors, thereby enabling controllable
object-level reasoning. This eliminates the necessity of fusing a lengthy array
of image patch features and significantly speeds up training. Furthermore, we
propose region-level retrieval using our object representations, facilitating
rapid adaptation to new objects without additional training. Our experiments
reveal that our method achieves competitive referring object classification and
captioning performance, while also offering zero-shot generalization and
robustness to visually challenging contexts.
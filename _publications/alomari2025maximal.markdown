---
layout: publication
title: 'Maximal Matching Matters: Preventing Representation Collapse For Robust Cross-modal
  Retrieval'
authors: Hani Alomari, Anushka Sivakumar, Andrew Zhang, Chris Thomas
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2025
bibkey: alomari2025maximal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.21538'}]
tags: ["Evaluation", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Alomari et al.
---
Cross-modal image-text retrieval is challenging because of the diverse possible associations between content from different modalities. Traditional methods learn a single-vector embedding to represent semantics of each sample, but struggle to capture nuanced and diverse relationships that can exist across modalities. Set-based approaches, which represent each sample with multiple embeddings, offer a promising alternative, as they can capture richer and more diverse relationships. In this paper, we show that, despite their promise, these set-based representations continue to face issues including sparse supervision and set collapse, which limits their effectiveness. To address these challenges, we propose Maximal Pair Assignment Similarity to optimize one-to-one matching between embedding sets which preserve semantic diversity within the set. We also introduce two loss functions to further enhance the representations: Global Discriminative Loss to enhance distinction among embeddings, and Intra-Set Divergence Loss to prevent collapse within each set. Our method achieves state-of-the-art performance on MS-COCO and Flickr30k without relying on external data.
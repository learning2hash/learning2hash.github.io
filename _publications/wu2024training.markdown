---
layout: publication
title: Training-free Zero-shot Composed Image Retrieval Via Weighted Modality Fusion
  And Similarity
authors: Ren-di Wu, Yu-Yen Lin, Huei-Fang Yang
conference: Technologies and Applications of Artificial Intelligence pp. 77-90 Springer
  2025
year: 2024
bibkey: wu2024training
citations: 0
additional_links: [{name: Code, url: 'https://github.com/whats2000/WeiMoCIR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2409.04918'}]
tags: [Evaluation, Supervised, Image Retrieval, Few-shot & Zero-shot, Datasets, Scalability]
short_authors: Ren-di Wu, Yu-Yen Lin, Huei-Fang Yang
---
Composed image retrieval (CIR), which formulates the query as a combination
of a reference image and modified text, has emerged as a new form of image
search due to its enhanced ability to capture user intent. However, training a
CIR model in a supervised manner typically requires labor-intensive collection
of (reference image, text modifier, target image) triplets. While existing
zero-shot CIR (ZS-CIR) methods eliminate the need for training on specific
downstream datasets, they still require additional pretraining on large-scale
image datasets. In this paper, we introduce a training-free approach for
ZS-CIR. Our approach, Weighted Modality fusion and similarity for CIR
(WeiMoCIR), operates under the assumption that image and text modalities can be
effectively combined using a simple weighted average. This allows the query
representation to be constructed directly from the reference image and text
modifier. To further enhance retrieval performance, we employ multimodal large
language models (MLLMs) to generate image captions for the database images and
incorporate these textual captions into the similarity computation by combining
them with image information using a weighted average. Our approach is simple,
easy to implement, and its effectiveness is validated through experiments on
the FashionIQ and CIRR datasets. Code is available at
https://github.com/whats2000/WeiMoCIR.
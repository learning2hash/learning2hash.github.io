---
layout: publication
title: Polysemous Visual-semantic Embedding For Cross-modal Retrieval
authors: Yale Song, Mohammad Soleymani
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: song2019polysemous
citations: 223
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.04402'}]
tags: ["CVPR", "Datasets", "Evaluation", "Multimodal Retrieval", "Text Retrieval", "Tools & Libraries"]
short_authors: Yale Song, Mohammad Soleymani
---
Visual-semantic embedding aims to find a shared latent space where related
visual and textual instances are close to each other. Most current methods
learn injective embedding functions that map an instance to a single point in
the shared space. Unfortunately, injective embedding cannot effectively handle
polysemous instances with multiple possible meanings; at best, it would find an
average representation of different meanings. This hinders its use in
real-world scenarios where individual instances and their cross-modal
associations are often ambiguous. In this work, we introduce Polysemous
Instance Embedding Networks (PIE-Nets) that compute multiple and diverse
representations of an instance by combining global context with locally-guided
features via multi-head self-attention and residual learning. To learn
visual-semantic embedding, we tie-up two PIE-Nets and optimize them jointly in
the multiple instance learning framework. Most existing work on cross-modal
retrieval focuses on image-text data. Here, we also tackle a more challenging
case of video-text retrieval. To facilitate further research in video-text
retrieval, we release a new dataset of 50K video-sentence pairs collected from
social media, dubbed MRW (my reaction when). We demonstrate our approach on
both image-text and video-text retrieval scenarios using MS-COCO, TGIF, and our
new MRW dataset.
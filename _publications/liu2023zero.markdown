---
layout: publication
title: Zero-shot Composed Text-image Retrieval
authors: Yikun Liu, Jiangchao Yao, Ya Zhang, Yanfeng Wang, Weidi Xie
conference: Arxiv
year: 2023
bibkey: liu2023zero
citations: 1
additional_links: [{name: Code, url: 'https://code-kunkun'}, {name: Paper, url: 'https://arxiv.org/abs/2306.07272'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Image Retrieval", "Scalability"]
short_authors: Liu et al.
---
In this paper, we consider the problem of composed image retrieval (CIR), it
aims to train a model that can fuse multi-modal information, e.g., text and
images, to accurately retrieve images that match the query, extending the
user's expression ability. We make the following contributions: (i) we initiate
a scalable pipeline to automatically construct datasets for training CIR model,
by simply exploiting a large-scale dataset of image-text pairs, e.g., a subset
of LAION-5B; (ii) we introduce a transformer-based adaptive aggregation model,
TransAgg, which employs a simple yet efficient fusion mechanism, to adaptively
combine information from diverse modalities; (iii) we conduct extensive
ablation studies to investigate the usefulness of our proposed data
construction procedure, and the effectiveness of core components in TransAgg;
(iv) when evaluating on the publicly available benckmarks under the zero-shot
scenario, i.e., training on the automatically constructed datasets, then
directly conduct inference on target downstream datasets, e.g., CIRR and
FashionIQ, our proposed approach either performs on par with or significantly
outperforms the existing state-of-the-art (SOTA) models. Project page:
https://code-kunkun.github.io/ZS-CIR/
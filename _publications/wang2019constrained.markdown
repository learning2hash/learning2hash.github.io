---
layout: publication
title: Constrained Non-affine Alignment Of Embeddings
authors: Yuwei Wang, Yan Zheng, Yanqing Peng, Chin-chia Michael Yeh, Zhongfang Zhuang,
  Das Mahashweta, Bendre Mangesh, Feifei Li, Wei Zhang, Jeff M. Phillips
conference: 2021 IEEE International Conference on Data Mining (ICDM)
year: 2021
bibkey: wang2019constrained
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.05862'}]
tags: ["Robustness"]
short_authors: Wang et al.
---
Embeddings are one of the fundamental building blocks for data analysis
tasks. Embeddings are already essential tools for large language models and
image analysis, and their use is being extended to many other research domains.
The generation of these distributed representations is often a data- and
computation-expensive process; yet the holistic analysis and adjustment of them
after they have been created is still a developing area. In this paper, we
first propose a very general quantitatively measure for the presence of
features in the embedding data based on if it can be learned. We then devise a
method to remove or alleviate undesired features in the embedding while
retaining the essential structure of the data. We use a Domain Adversarial
Network (DAN) to generate a non-affine transformation, but we add constraints
to ensure the essential structure of the embedding is preserved. Our empirical
results demonstrate that the proposed algorithm significantly outperforms the
state-of-art unsupervised algorithm on several data sets, including novel
applications from the industry.
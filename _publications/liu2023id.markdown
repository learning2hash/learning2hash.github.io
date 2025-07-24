---
layout: publication
title: ID Embedding As Subtle Features Of Content And Structure For Multimodal Recommendation
authors: Yuting Liu, Enneng Yang, Yizhou Dang, Guibing Guo, Qiang Liu, Yuliang Liang,
  Linying Jiang, Xingwei Wang
conference: Arxiv
year: 2023
bibkey: liu2023id
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.05956'}]
tags: ["Datasets", "Evaluation", "Recommender Systems", "Self-Supervised"]
short_authors: Liu et al.
---
Multimodal recommendation aims to model user and item representations
comprehensively with the involvement of multimedia content for effective
recommendations. Existing research has shown that it is beneficial for
recommendation performance to combine (user- and item-) ID embeddings with
multimodal salient features, indicating the value of IDs. However, there is a
lack of a thorough analysis of the ID embeddings in terms of feature semantics
in the literature. In this paper, we revisit the value of ID embeddings for
multimodal recommendation and conduct a thorough study regarding its semantics,
which we recognize as subtle features of *content* and *structure*.
Based on our findings, we propose a novel recommendation model by incorporating
ID embeddings to enhance the salient features of both content and structure.
Specifically, we put forward a hierarchical attention mechanism to incorporate
ID embeddings in modality fusing, coupled with contrastive learning, to enhance
content representations. Meanwhile, we propose a lightweight graph convolution
network for each modality to amalgamate neighborhood and ID embeddings for
improving structural representations. Finally, the content and structure
representations are combined to form the ultimate item embedding for
recommendation. Extensive experiments on three real-world datasets (Baby,
Sports, and Clothing) demonstrate the superiority of our method over
state-of-the-art multimodal recommendation methods and the effectiveness of
fine-grained ID embeddings. Our code is available at
https://anonymous.4open.science/r/IDSF-code/.
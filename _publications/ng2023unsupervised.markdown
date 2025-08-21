---
layout: publication
title: Unsupervised Hashing With Similarity Distribution Calibration
authors: Kam Woh Ng, Xiatian Zhu, Jiun Tian Hoe, Chee Seng Chan, Tianyu Zhang, Yi-Zhe
  Song, Tao Xiang
conference: Arxiv
year: 2023
bibkey: ng2023unsupervised
citations: 0
additional_links: [{name: Code, url: 'https://github.com/kamwoh/sdc.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2302.07669'}]
tags: ["Hashing Methods", "Supervised", "Unsupervised"]
short_authors: Ng et al.
---
Unsupervised hashing methods typically aim to preserve the similarity between
data points in a feature space by mapping them to binary hash codes. However,
these methods often overlook the fact that the similarity between data points
in the continuous feature space may not be preserved in the discrete hash code
space, due to the limited similarity range of hash codes. The similarity range
is bounded by the code length and can lead to a problem known as similarity
collapse. That is, the positive and negative pairs of data points become less
distinguishable from each other in the hash space. To alleviate this problem,
in this paper a novel Similarity Distribution Calibration (SDC) method is
introduced. SDC aligns the hash code similarity distribution towards a
calibration distribution (e.g., beta distribution) with sufficient spread
across the entire similarity range, thus alleviating the similarity collapse
problem. Extensive experiments show that our SDC outperforms significantly the
state-of-the-art alternatives on coarse category-level and instance-level image
retrieval. Code is available at https://github.com/kamwoh/sdc.
---
layout: publication
title: Contextually Affinitive Neighborhood Refinery For Deep Clustering
authors: Yu Chunlin, Shi Ye, Wang Jingya
conference: Arxiv
year: 2023
bibkey: yu2023contextually
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.07806'}]
tags: ["Distance Metric Learning", "Hybrid ANN Methods", "Scalability", "Self-Supervised", "Supervised"]
short_authors: Yu Chunlin, Shi Ye, Wang Jingya
---
Previous endeavors in self-supervised learning have enlightened the research
of deep clustering from an instance discrimination perspective. Built upon this
foundation, recent studies further highlight the importance of grouping
semantically similar instances. One effective method to achieve this is by
promoting the semantic structure preserved by neighborhood consistency.
However, the samples in the local neighborhood may be limited due to their
close proximity to each other, which may not provide substantial and diverse
supervision signals. Inspired by the versatile re-ranking methods in the
context of image retrieval, we propose to employ an efficient online re-ranking
process to mine more informative neighbors in a Contextually Affinitive
(ConAff) Neighborhood, and then encourage the cross-view neighborhood
consistency. To further mitigate the intrinsic neighborhood noises near cluster
boundaries, we propose a progressively relaxed boundary filtering strategy to
circumvent the issues brought by noisy neighbors. Our method can be easily
integrated into the generic self-supervised frameworks and outperforms the
state-of-the-art methods on several popular benchmarks.
---
layout: publication
title: Consistent Style Transfer
authors: Xuan Luo, Zhen Han, Lingkang Yang, Lingling Zhang
conference: Arxiv
year: 2022
bibkey: luo2022consistent
citations: 14
additional_links: [{name: Code, url: 'https://github.com/computer-vision2022/PAMA'},
  {name: Paper, url: 'https://arxiv.org/abs/2201.02233'}]
tags: ["Evaluation"]
short_authors: Luo et al.
---
Recently, attentional arbitrary style transfer methods have been proposed to
achieve fine-grained results, which manipulates the point-wise similarity
between content and style features for stylization. However, the attention
mechanism based on feature points ignores the feature multi-manifold
distribution, where each feature manifold corresponds to a semantic region in
the image. Consequently, a uniform content semantic region is rendered by
highly different patterns from various style semantic regions, producing
inconsistent stylization results with visual artifacts. We proposed the
progressive attentional manifold alignment (PAMA) to alleviate this problem,
which repeatedly applies attention operations and space-aware interpolations.
The attention operation rearranges style features dynamically according to the
spatial distribution of content features. This makes the content and style
manifolds correspond on the feature map. Then the space-aware interpolation
adaptively interpolates between the corresponding content and style manifolds
to increase their similarity. By gradually aligning the content manifolds to
style manifolds, the proposed PAMA achieves state-of-the-art performance while
avoiding the inconsistency of semantic regions. Codes are available at
https://github.com/computer-vision2022/PAMA.
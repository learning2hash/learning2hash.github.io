---
layout: publication
title: 'FUSELOC: Fusing Global And Local Descriptors To Disambiguate 2D-3D Matching
  In Visual Localization'
authors: Son Tung Nguyen, Alejandro Fontan, Michael Milford, Tobias Fischer
conference: Arxiv
year: 2024
bibkey: nguyen2024fuseloc
citations: 0
additional_links: [{name: Code, url: 'https://github.com/sontung/descriptor-disambiguation\}\{github.com/sontung/descriptor-disambiguation\'},
  {name: Paper, url: 'https://arxiv.org/abs/2408.12037'}]
tags: []
short_authors: Nguyen et al.
---
Hierarchical methods represent state-of-the-art visual localization,
optimizing search efficiency by using global descriptors to focus on relevant
map regions. However, this state-of-the-art performance comes at the cost of
substantial memory requirements, as all database images must be stored for
feature matching. In contrast, direct 2D-3D matching algorithms require
significantly less memory but suffer from lower accuracy due to the larger and
more ambiguous search space. We address this ambiguity by fusing local and
global descriptors using a weighted average operator within a 2D-3D search
framework. This fusion rearranges the local descriptor space such that
geographically nearby local descriptors are closer in the feature space
according to the global descriptors. Therefore, the number of irrelevant
competing descriptors decreases, specifically if they are geographically
distant, thereby increasing the likelihood of correctly matching a query
descriptor. We consistently improve the accuracy over local-only systems and
achieve performance close to hierarchical methods while halving memory
requirements. Extensive experiments using various state-of-the-art local and
global descriptors across four different datasets demonstrate the effectiveness
of our approach. For the first time, our approach enables direct matching
algorithms to benefit from global descriptors while maintaining memory
efficiency. The code for this paper will be published at
\href\{https://github.com/sontung/descriptor-disambiguation\}\{github.com/sontung/descriptor-disambiguation\}.
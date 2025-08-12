---
layout: publication
title: 'Co-occurrence Matters: Learning Action Relation For Temporal Action Localization'
authors: Congqi Cao, Yizhe Wang, Yue Lu, Xin Zhang, Yanning Zhang
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2023
bibkey: cao2023co
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.08463'}]
tags: []
short_authors: Cao et al.
---
Temporal action localization (TAL) is a prevailing task due to its great
application potential. Existing works in this field mainly suffer from two
weaknesses: (1) They often neglect the multi-label case and only focus on
temporal modeling. (2) They ignore the semantic information in class labels and
only use the visual information. To solve these problems, we propose a novel
Co-Occurrence Relation Module (CORM) that explicitly models the co-occurrence
relationship between actions. Besides the visual information, it further
utilizes the semantic embeddings of class labels to model the co-occurrence
relationship. The CORM works in a plug-and-play manner and can be easily
incorporated with the existing sequence models. By considering both visual and
semantic co-occurrence, our method achieves high multi-label relationship
modeling capacity. Meanwhile, existing datasets in TAL always focus on
low-semantic atomic actions. Thus we construct a challenging multi-label
dataset UCF-Crime-TAL that focuses on high-semantic actions by annotating the
UCF-Crime dataset at frame level and considering the semantic overlap of
different events. Extensive experiments on two commonly used TAL datasets,
\textit\{i.e.\}, MultiTHUMOS and TSU, and our newly proposed UCF-Crime-TAL
demenstrate the effectiveness of the proposed CORM, which achieves
state-of-the-art performance on these datasets.
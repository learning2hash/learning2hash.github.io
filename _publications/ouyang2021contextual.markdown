---
layout: publication
title: Contextual Similarity Aggregation With Self-attention For Visual Re-ranking
authors: Jianbo Ouyang, Hui Wu, Min Wang, Wengang Zhou, Houqiang Li
conference: Arxiv
year: 2021
bibkey: ouyang2021contextual
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.13430'}]
tags: ["Image Retrieval", "Re-Ranking", "Robustness"]
short_authors: Ouyang et al.
---
In content-based image retrieval, the first-round retrieval result by simple
visual feature comparison may be unsatisfactory, which can be refined by visual
re-ranking techniques. In image retrieval, it is observed that the contextual
similarity among the top-ranked images is an important clue to distinguish the
semantic relevance. Inspired by this observation, in this paper, we propose a
visual re-ranking method by contextual similarity aggregation with
self-attention. In our approach, for each image in the top-K ranking list, we
represent it into an affinity feature vector by comparing it with a set of
anchor images. Then, the affinity features of the top-K images are refined by
aggregating the contextual information with a transformer encoder. Finally, the
affinity features are used to recalculate the similarity scores between the
query and the top-K images for re-ranking of the latter. To further improve the
robustness of our re-ranking model and enhance the performance of our method, a
new data augmentation scheme is designed. Since our re-ranking model is not
directly involved with the visual feature used in the initial retrieval, it is
ready to be applied to retrieval result lists obtained from various retrieval
algorithms. We conduct comprehensive experiments on four benchmark datasets to
demonstrate the generality and effectiveness of our proposed visual re-ranking
method.
---
layout: publication
title: 'Swamp: Swapped Assignment Of Multi-modal Pairs For Cross-modal Retrieval'
authors: Minyoung Kim
conference: "Arxiv"
year: 2021
citations: 0
bibkey: kim2021swapped
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2111.05814'}
tags: ['Cross-Modal', 'Deep', 'Retrieval Models', 'Supervised', 'Training Strategy', 'Applications']
---
We tackle the cross-modal retrieval problem, where learning is only
supervised by relevant multi-modal pairs in the data. Although the contrastive
learning is the most popular approach for this task, it makes potentially wrong
assumption that the instances in different pairs are automatically irrelevant.
To address the issue, we propose a novel loss function that is based on
self-labeling of the unknown semantic classes. Specifically, we aim to predict
class labels of the data instances in each modality, and assign those labels to
the corresponding instances in the other modality (i.e., swapping the pseudo
labels). With these swapped labels, we learn the data embedding for each
modality using the supervised cross-entropy loss. This way, cross-modal
instances from different pairs that are semantically related can be aligned to
each other by the class predictor. We tested our approach on several real-world
cross-modal retrieval problems, including text-based video retrieval,
sketch-based image retrieval, and image-text retrieval. For all these tasks our
method achieves significant performance improvement over the contrastive
learning.

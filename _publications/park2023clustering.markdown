---
layout: publication
title: Clustering-based Image-text Graph Matching For Domain Generalization
authors: Nokyung Park, Daewon Chae, Jeongyong Shim, Sangpil Kim, Eun-sol Kim, Jinkyu
  Kim
conference: Lecture Notes in Computer Science
year: 2024
bibkey: park2023clustering
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.02692'}]
tags: ["Datasets", "Evaluation"]
short_authors: Park et al.
---
Learning domain-invariant visual representations is important to train a
model that can generalize well to unseen target task domains. Recent works
demonstrate that text descriptions contain high-level class-discriminative
information and such auxiliary semantic cues can be used as effective pivot
embedding for domain generalization problems. However, they use pivot embedding
in a global manner (i.e., aligning an image embedding with sentence-level text
embedding), which does not fully utilize the semantic cues of given text
description. In this work, we advocate for the use of local alignment between
image regions and corresponding textual descriptions to get domain-invariant
features. To this end, we first represent image and text inputs as graphs. We
then cluster nodes within these graphs and match the graph-based image node
features to the nodes of textual graphs. This matching process is conducted
both globally and locally, tightly aligning visual and textual semantic
sub-structures. We experiment with large-scale public datasets, such as CUB-DG
and DomainBed, and our model achieves matched or better state-of-the-art
performance on these datasets. The code is available at:
https://github.com/noparkee/Graph-Clustering-based-DG
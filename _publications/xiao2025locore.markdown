---
layout: publication
title: 'LOCORE: Image Re-ranking With Long-context Sequence Modeling'
authors: Xiao et al.
conference: Proceedings of the ACM International Conference on Image and Video Retrieval
year: 2025
bibkey: xiao2025locore
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.21772'}]
tags: ["Hybrid-ANN-Methods", "Video-Retrieval", "Re-Ranking"]
---
We introduce LOCORE, Long-Context Re-ranker, a model that takes as input
local descriptors corresponding to an image query and a list of gallery images
and outputs similarity scores between the query and each gallery image. This
model is used for image retrieval, where typically a first ranking is performed
with an efficient similarity measure, and then a shortlist of top-ranked images
is re-ranked based on a more fine-grained similarity measure. Compared to
existing methods that perform pair-wise similarity estimation with local
descriptors or list-wise re-ranking with global descriptors, LOCORE is the
first method to perform list-wise re-ranking with local descriptors. To achieve
this, we leverage efficient long-context sequence models to effectively capture
the dependencies between query and gallery images at the local-descriptor
level. During testing, we process long shortlists with a sliding window
strategy that is tailored to overcome the context size limitations of sequence
models. Our approach achieves superior performance compared with other
re-rankers on established image retrieval benchmarks of landmarks (ROxf and
RPar), products (SOP), fashion items (In-Shop), and bird species (CUB-200)
while having comparable latency to the pair-wise local descriptor re-rankers.
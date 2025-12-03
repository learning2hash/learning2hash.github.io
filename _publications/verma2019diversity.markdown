---
layout: publication
title: Diversity In Fashion Recommendation Using Semantic Parsing
authors: Sagar Verma, Sukhad Anand, Chetan Arora, Atul Rai
conference: Arxiv
year: 2019
bibkey: verma2019diversity
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.08292'}]
tags: ["Datasets", "Recommender Systems", "Supervised"]
short_authors: Verma et al.
---
Developing recommendation system for fashion images is challenging due to the
inherent ambiguity associated with what criterion a user is looking at.
Suggesting multiple images where each output image is similar to the query
image on the basis of a different feature or part is one way to mitigate the
problem. Existing works for fashion recommendation have used Siamese or Triplet
network to learn features between a similar pair and a similar-dissimilar
triplet respectively. However, these methods do not provide basic information
such as, how two clothing images are similar, or which parts present in the two
images make them similar. In this paper, we propose to recommend images by
explicitly learning and exploiting part based similarity. We propose a novel
approach of learning discriminative features from weakly-supervised data by
using visual attention over the parts and a texture encoding network. We show
that the learned features surpass the state-of-the-art in retrieval task on
DeepFashion dataset. We then use the proposed model to recommend fashion images
having an explicit variation with respect to similarity of any of the parts.
---
layout: publication
title: Learning To Hash With Semantic Similarity Metrics And Empirical KL Divergence
authors: Heikki Arponen, Tom E. Bishop
conference: Arxiv
year: 2020
bibkey: arponen2020learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.04917'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Supervised"]
short_authors: Heikki Arponen, Tom E. Bishop
---
Learning to hash is an efficient paradigm for exact and approximate nearest
neighbor search from massive databases. Binary hash codes are typically
extracted from an image by rounding output features from a CNN, which is
trained on a supervised binary similar/ dissimilar task. Drawbacks of this
approach are: (i) resulting codes do not necessarily capture semantic
similarity of the input data (ii) rounding results in information loss,
manifesting as decreased retrieval performance and (iii) Using only class-wise
similarity as a target can lead to trivial solutions, simply encoding
classifier outputs rather than learning more intricate relations, which is not
detected by most performance metrics. We overcome (i) via a novel loss function
encouraging the relative hash code distances of learned features to match those
derived from their targets. We address (ii) via a differentiable estimate of
the KL divergence between network outputs and a binary target distribution,
resulting in minimal information loss when the features are rounded to binary.
Finally, we resolve (iii) by focusing on a hierarchical precision metric.
Efficiency of the methods is demonstrated with semantic image retrieval on the
CIFAR-100, ImageNet and Conceptual Captions datasets, using similarities
inferred from the WordNet label hierarchy or sentence embeddings.
---
layout: publication
title: Feature And Label Embedding Spaces Matter In Addressing Image Classifier Bias
authors: William Thong, Cees G. M. Snoek
conference: Arxiv
year: 2021
bibkey: thong2021feature
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.14336'}]
tags: []
short_authors: William Thong, Cees G. M. Snoek
---
This paper strives to address image classifier bias, with a focus on both
feature and label embedding spaces. Previous works have shown that spurious
correlations from protected attributes, such as age, gender, or skin tone, can
cause adverse decisions. To balance potential harms, there is a growing need to
identify and mitigate image classifier bias. First, we identify in the feature
space a bias direction. We compute class prototypes of each protected attribute
value for every class, and reveal an existing subspace that captures the
maximum variance of the bias. Second, we mitigate biases by mapping image
inputs to label embedding spaces. Each value of the protected attribute has its
projection head where classes are embedded through a latent vector
representation rather than a common one-hot encoding. Once trained, we further
reduce in the feature space the bias effect by removing its direction.
Evaluation on biased image datasets, for multi-class, multi-label and binary
classifications, shows the effectiveness of tackling both feature and label
embedding spaces in improving the fairness of the classifier predictions, while
preserving classification performance.
---
layout: publication
title: Sample-specific Debiasing For Better Image-text Models
authors: Peiqi Wang, Yingcheng Liu, Ching-Yun Ko, William M. Wells, Seth Berkowitz,
  Steven Horng, Polina Golland
conference: Arxiv
year: 2023
bibkey: wang2023sample
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.13181'}]
tags: [Self-Supervised, Supervised, Multimodal Retrieval]
short_authors: Wang et al.
---
Self-supervised representation learning on image-text data facilitates
crucial medical applications, such as image classification, visual grounding,
and cross-modal retrieval. One common approach involves contrasting
semantically similar (positive) and dissimilar (negative) pairs of data points.
Drawing negative samples uniformly from the training data set introduces false
negatives, i.e., samples that are treated as dissimilar but belong to the same
class. In healthcare data, the underlying class distribution is nonuniform,
implying that false negatives occur at a highly variable rate. To improve the
quality of learned representations, we develop a novel approach that corrects
for false negatives. Our method can be viewed as a variant of debiased
contrastive learning that uses estimated sample-specific class probabilities.
We provide theoretical analysis of the objective function and demonstrate the
proposed approach on both image and paired image-text data sets. Our
experiments illustrate empirical advantages of sample-specific debiasing.
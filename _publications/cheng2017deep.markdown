---
layout: publication
title: Deep Feature Learning Via Structured Graph Laplacian Embedding For Person Re-identification
authors: de Cheng, Yihong Gong, Zhihui Li, Weiwei Shi, Alexander G. Hauptmann, Nanning
  Zheng
conference: Pattern Recognition
year: 2018
bibkey: cheng2017deep
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07791'}]
tags: [Evaluation, Distance Metric Learning, Datasets, CVPR]
short_authors: Cheng et al.
---
Learning the distance metric between pairs of examples is of great importance
for visual recognition, especially for person re-identification (Re-Id).
Recently, the contrastive and triplet loss are proposed to enhance the
discriminative power of the deeply learned features, and have achieved
remarkable success. As can be seen, either the contrastive or triplet loss is
just one special case of the Euclidean distance relationships among these
training samples. Therefore, we propose a structured graph Laplacian embedding
algorithm, which can formulate all these structured distance relationships into
the graph Laplacian form. The proposed method can take full advantages of the
structured distance relationships among these training samples, with the
constructed complete graph. Besides, this formulation makes our method
easy-to-implement and super-effective. When embedding the proposed algorithm
with the softmax loss for the CNN training, our method can obtain much more
robust and discriminative deep features with inter-personal dispersion and
intra-personal compactness, which is essential to person Re-Id. We illustrate
the effectiveness of our proposed method on top of three popular networks,
namely AlexNet, DGDNet and ResNet50, on recent four widely used Re-Id benchmark
datasets. Our proposed method achieves state-of-the-art performances.
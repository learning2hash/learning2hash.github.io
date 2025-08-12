---
layout: publication
title: An Empirical Study Into Clustering Of Unseen Datasets With Self-supervised
  Encoders
authors: Scott C. Lowe, Joakim Bruslund Haurum, Sageev Oore, Thomas B. Moeslund, Graham
  W. Taylor
conference: Arxiv
year: 2024
bibkey: lowe2024empirical
citations: 1
additional_links: [{name: Code, url: 'https://github.com/scottclowe/zs-ssl-clustering/'},
  {name: Paper, url: 'https://arxiv.org/abs/2406.02465'}]
tags: ["Datasets", "Self-Supervised"]
short_authors: Lowe et al.
---
Can pretrained models generalize to new datasets without any retraining? We
deploy pretrained image models on datasets they were not trained for, and
investigate whether their embeddings form meaningful clusters. Our suite of
benchmarking experiments use encoders pretrained solely on ImageNet-1k with
either supervised or self-supervised training techniques, deployed on image
datasets that were not seen during training, and clustered with conventional
clustering algorithms. This evaluation provides new insights into the
embeddings of self-supervised models, which prioritize different features to
supervised models. Supervised encoders typically offer more utility than SSL
encoders within the training domain, and vice-versa far outside of it, however,
fine-tuned encoders demonstrate the opposite trend. Clustering provides a way
to evaluate the utility of self-supervised learned representations orthogonal
to existing methods such as kNN. Additionally, we find the silhouette score
when measured in a UMAP-reduced space is highly correlated with clustering
performance, and can therefore be used as a proxy for clustering performance on
data with no ground truth labels. Our code implementation is available at
https://github.com/scottclowe/zs-ssl-clustering/.
---
layout: publication
title: Cluster Analysis With Deep Embeddings And Contrastive Learning
authors: Ramakrishnan Sundareswaran, Jansel Herrera-Gerena, John Just, Ali Jannesari
conference: Arxiv
year: 2021
bibkey: sundareswaran2021cluster
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.12714'}]
tags: ["Distance Metric Learning", "Self-Supervised", "Unsupervised"]
short_authors: Sundareswaran et al.
---
Unsupervised disentangled representation learning is a long-standing problem
in computer vision. This work proposes a novel framework for performing image
clustering from deep embeddings by combining instance-level contrastive
learning with a deep embedding based cluster center predictor. Our approach
jointly learns representations and predicts cluster centers in an end-to-end
manner. This is accomplished via a three-pronged approach that combines a
clustering loss, an instance-wise contrastive loss, and an anchor loss. Our
fundamental intuition is that using an ensemble loss that incorporates
instance-level features and a clustering procedure focusing on semantic
similarity reinforces learning better representations in the latent space. We
observe that our method performs exceptionally well on popular vision datasets
when evaluated using standard clustering metrics such as Normalized Mutual
Information (NMI), in addition to producing geometrically well-separated
cluster embeddings as defined by the Euclidean distance. Our framework performs
on par with widely accepted clustering methods and outperforms the
state-of-the-art contrastive learning method on the CIFAR-10 dataset with an
NMI score of 0.772, a 7-8% improvement on the strong baseline.
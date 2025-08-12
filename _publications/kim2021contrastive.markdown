---
layout: publication
title: Contrastive Fine-grained Class Clustering Via Generative Adversarial Networks
authors: Yunji Kim, Jung-Woo Ha
conference: Arxiv
year: 2021
bibkey: kim2021contrastive
citations: 4
additional_links: [{name: Code, url: 'https://github.com/naver-ai/c3-gan'}, {name: Paper,
    url: 'https://arxiv.org/abs/2112.14971'}]
tags: ["Distance Metric Learning", "Self-Supervised", "Unsupervised"]
short_authors: Yunji Kim, Jung-Woo Ha
---
Unsupervised fine-grained class clustering is a practical yet challenging
task due to the difficulty of feature representations learning of subtle object
details. We introduce C3-GAN, a method that leverages the categorical inference
power of InfoGAN with contrastive learning. We aim to learn feature
representations that encourage a dataset to form distinct cluster boundaries in
the embedding space, while also maximizing the mutual information between the
latent code and its image observation. Our approach is to train a
discriminator, which is also used for inferring clusters, to optimize the
contrastive loss, where image-latent pairs that maximize the mutual information
are considered as positive pairs and the rest as negative pairs. Specifically,
we map the input of a generator, which was sampled from the categorical
distribution, to the embedding space of the discriminator and let them act as a
cluster centroid. In this way, C3-GAN succeeded in learning a
clustering-friendly embedding space where each cluster is distinctively
separable. Experimental results show that C3-GAN achieved the state-of-the-art
clustering performance on four fine-grained image datasets, while also
alleviating the mode collapse phenomenon. Code is available at
https://github.com/naver-ai/c3-gan.
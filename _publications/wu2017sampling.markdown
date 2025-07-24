---
layout: publication
title: Sampling Matters In Deep Embedding Learning
authors: "Chao-yuan Wu, R. Manmatha, Alexander J. Smola, Philipp Kr\xE4henb\xFChl"
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: wu2017sampling
citations: 863
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.07567'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot", "ICCV", "Image Retrieval"]
short_authors: Wu et al.
---
Deep embeddings answer one simple question: How similar are two images?
Learning these embeddings is the bedrock of verification, zero-shot learning,
and visual search. The most prominent approaches optimize a deep convolutional
network with a suitable loss function, such as contrastive loss or triplet
loss. While a rich line of work focuses solely on the loss functions, we show
in this paper that selecting training examples plays an equally important role.
We propose distance weighted sampling, which selects more informative and
stable examples than traditional approaches. In addition, we show that a simple
margin based loss is sufficient to outperform all other loss functions. We
evaluate our approach on the Stanford Online Products, CAR196, and the
CUB200-2011 datasets for image retrieval and clustering, and on the LFW dataset
for face verification. Our method achieves state-of-the-art performance on all
of them.
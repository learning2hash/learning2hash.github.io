---
layout: publication
title: Hashing With Mutual Information
authors: Fatih Cakir, Kun He, Sarah Adel Bargal, Stan Sclaroff
conference: Lecture Notes in Computer Science
year: 2018
bibkey: cakir2018hashing
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.00974'}]
tags: ["Evaluation", "Hashing Methods", "Image Retrieval", "Supervised", "Video Retrieval"]
short_authors: Cakir et al.
---
Binary vector embeddings enable fast nearest neighbor retrieval in large
databases of high-dimensional objects, and play an important role in many
practical applications, such as image and video retrieval. We study the problem
of learning binary vector embeddings under a supervised setting, also known as
hashing. We propose a novel supervised hashing method based on optimizing an
information-theoretic quantity: mutual information. We show that optimizing
mutual information can reduce ambiguity in the induced neighborhood structure
in the learned Hamming space, which is essential in obtaining high retrieval
performance. To this end, we optimize mutual information in deep neural
networks with minibatch stochastic gradient descent, with a formulation that
maximally and efficiently utilizes available supervision. Experiments on four
image retrieval benchmarks, including ImageNet, confirm the effectiveness of
our method in learning high-quality binary embeddings for nearest neighbor
retrieval.
---
layout: publication
title: Unifying Specialist Image Embedding Into Universal Image Embedding
authors: Feng et al.
conference: Arxiv
year: 2020
bibkey: feng2020unifying
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.03701'}]
---
Deep image embedding provides a way to measure the semantic similarity of two
images. It plays a central role in many applications such as image search, face
verification, and zero-shot learning. It is desirable to have a universal deep
embedding model applicable to various domains of images. However, existing
methods mainly rely on training specialist embedding models each of which is
applicable to images from a single domain. In this paper, we study an important
but unexplored task: how to train a single universal image embedding model to
match the performance of several specialists on each specialist's domain.
Simply fusing the training data from multiple domains cannot solve this problem
because some domains become overfitted sooner when trained together using
existing methods. Therefore, we propose to distill the knowledge in multiple
specialists into a universal embedding to solve this problem. In contrast to
existing embedding distillation methods that distill the absolute distances
between images, we transform the absolute distances between images into a
probabilistic distribution and minimize the KL-divergence between the
distributions of the specialists and the universal embedding. Using several
public datasets, we validate that our proposed method accomplishes the goal of
universal image embedding.
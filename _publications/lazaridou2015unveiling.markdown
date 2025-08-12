---
layout: publication
title: 'Unveiling The Dreams Of Word Embeddings: Towards Language-driven Image Generation'
authors: Angeliki Lazaridou, Dat Tien Nguyen, Raffaella Bernardi, Marco Baroni
conference: Arxiv
year: 2015
bibkey: lazaridou2015unveiling
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.03500'}]
tags: ["Multimodal Retrieval"]
short_authors: Lazaridou et al.
---
We introduce language-driven image generation, the task of generating an
image visualizing the semantic contents of a word embedding, e.g., given the
word embedding of grasshopper, we generate a natural image of a grasshopper. We
implement a simple method based on two mapping functions. The first takes as
input a word embedding (as produced, e.g., by the word2vec toolkit) and maps it
onto a high-level visual space (e.g., the space defined by one of the top
layers of a Convolutional Neural Network). The second function maps this
abstract visual representation to pixel space, in order to generate the target
image. Several user studies suggest that the current system produces images
that capture general visual properties of the concepts encoded in the word
embedding, such as color or typical environment, and are sufficient to
discriminate between general categories of objects.
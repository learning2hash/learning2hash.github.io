---
layout: publication
title: 'ASIC: Aligning Sparse In-the-wild Image Collections'
authors: Kamal Gupta, Varun Jampani, Carlos Esteves, Abhinav Shrivastava, Ameesh Makadia,
  Noah Snavely, Abhishek Kar
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: gupta2023asic
citations: 7
additional_links: [{name: Code, url: 'https://kampta.github.io/asic'}, {name: Paper,
    url: 'https://arxiv.org/abs/2303.16201'}]
tags: ["ICCV"]
short_authors: Gupta et al.
---
We present a method for joint alignment of sparse in-the-wild image
collections of an object category. Most prior works assume either ground-truth
keypoint annotations or a large dataset of images of a single object category.
However, neither of the above assumptions hold true for the long-tail of the
objects present in the world. We present a self-supervised technique that
directly optimizes on a sparse collection of images of a particular
object/object category to obtain consistent dense correspondences across the
collection. We use pairwise nearest neighbors obtained from deep features of a
pre-trained vision transformer (ViT) model as noisy and sparse keypoint matches
and make them dense and accurate matches by optimizing a neural network that
jointly maps the image collection into a learned canonical grid. Experiments on
CUB and SPair-71k benchmarks demonstrate that our method can produce globally
consistent and higher quality correspondences across the image collection when
compared to existing self-supervised methods. Code and other material will be
made available at https://kampta.github.io/asic.
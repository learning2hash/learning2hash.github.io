---
layout: publication
title: Matchable Image Retrieval By Learning From Surface Reconstruction
authors: Tianwei Shen, Zixin Luo, Lei Zhou, Runze Zhang, Siyu Zhu, Tian Fang, Long
  Quan
conference: Arxiv
year: 2018
bibkey: shen2018matchable
citations: 9
additional_links: [{name: Code, url: 'https://github.com/hlzz/mirror'}, {name: Paper,
    url: 'https://arxiv.org/abs/1811.10343'}]
tags: ["Image Retrieval", "Scalability"]
short_authors: Shen et al.
---
Convolutional Neural Networks (CNNs) have achieved superior performance on
object image retrieval, while Bag-of-Words (BoW) models with handcrafted local
features still dominate the retrieval of overlapping images in 3D
reconstruction. In this paper, we narrow down this gap by presenting an
efficient CNN-based method to retrieve images with overlaps, which we refer to
as the matchable image retrieval problem. Different from previous methods that
generates training data based on sparse reconstruction, we create a large-scale
image database with rich 3D geometrics and exploit information from surface
reconstruction to obtain fine-grained training data. We propose a batched
triplet-based loss function combined with mesh re-projection to effectively
learn the CNN representation. The proposed method significantly accelerates the
image retrieval process in 3D reconstruction and outperforms the
state-of-the-art CNN-based and BoW methods for matchable image retrieval. The
code and data are available at https://github.com/hlzz/mirror.
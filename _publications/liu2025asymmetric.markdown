---
layout: publication
title: Asymmetric Visual Semantic Embedding Framework For Efficient Vision-language
  Alignment
authors: Yang Liu, Mengyuan Liu, Shudong Huang, Jiancheng Lv
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: liu2025asymmetric
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.06974'}]
tags: ["AAAI", "Datasets", "Scalability", "Tools & Libraries"]
short_authors: Liu et al.
---
Learning visual semantic similarity is a critical challenge in bridging the
gap between images and texts. However, there exist inherent variations between
vision and language data, such as information density, i.e., images can contain
textual information from multiple different views, which makes it difficult to
compute the similarity between these two modalities accurately and efficiently.
In this paper, we propose a novel framework called Asymmetric Visual Semantic
Embedding (AVSE) to dynamically select features from various regions of images
tailored to different textual inputs for similarity calculation. To capture
information from different views in the image, we design a radial bias sampling
module to sample image patches and obtain image features from various views,
Furthermore, AVSE introduces a novel module for efficient computation of visual
semantic similarity between asymmetric image and text embeddings. Central to
this module is the presumption of foundational semantic units within the
embeddings, denoted as ``meta-semantic embeddings." It segments all embeddings
into meta-semantic embeddings with the same dimension and calculates visual
semantic similarity by finding the optimal match of meta-semantic embeddings of
two modalities. Our proposed AVSE model is extensively evaluated on the
large-scale MS-COCO and Flickr30K datasets, demonstrating its superiority over
recent state-of-the-art methods.
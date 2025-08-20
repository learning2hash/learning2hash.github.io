---
layout: publication
title: 'Visualsparta: An Embarrassingly Simple Approach To Large-scale Text-to-image
  Search With Weighted Bag-of-words'
authors: Xiaopeng Lu, Tiancheng Zhao, Kyusong Lee
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: lu2021visualsparta
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.00265'}]
tags: [Scalability, Multimodal Retrieval, Datasets, ACL, Efficiency, Image Retrieval]
short_authors: Xiaopeng Lu, Tiancheng Zhao, Kyusong Lee
---
Text-to-image retrieval is an essential task in cross-modal information
retrieval, i.e., retrieving relevant images from a large and unlabelled dataset
given textual queries. In this paper, we propose VisualSparta, a novel
(Visual-text Sparse Transformer Matching) model that shows significant
improvement in terms of both accuracy and efficiency. VisualSparta is capable
of outperforming previous state-of-the-art scalable methods in MSCOCO and
Flickr30K. We also show that it achieves substantial retrieving speed
advantages, i.e., for a 1 million image index, VisualSparta using CPU gets
~391X speedup compared to CPU vector search and ~5.4X speedup compared to
vector search with GPU acceleration. Experiments show that this speed advantage
even gets bigger for larger datasets because VisualSparta can be efficiently
implemented as an inverted index. To the best of our knowledge, VisualSparta is
the first transformer-based text-to-image retrieval model that can achieve
real-time searching for large-scale datasets, with significant accuracy
improvement compared to previous state-of-the-art methods.
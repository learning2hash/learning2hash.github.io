---
layout: publication
title: Transformer Reasoning Network for Image-Text Matching and Retrieval
authors: Messina Nicola, Falchi Fabrizio, Esuli Andrea, Amato Giuseppe
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: messina2020transformer
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.09144'}]
tags: ["Datasets", "Scalability", "Image-Retrieval"]
short_authors: Messina et al.
---
Image-text matching is an interesting and fascinating task in modern AI
research. Despite the evolution of deep-learning-based image and text
processing systems, multi-modal matching remains a challenging problem. In this
work, we consider the problem of accurate image-text matching for the task of
multi-modal large-scale information retrieval. State-of-the-art results in
image-text matching are achieved by inter-playing image and text features from
the two different processing pipelines, usually using mutual attention
mechanisms. However, this invalidates any chance to extract separate visual and
textual features needed for later indexing steps in large-scale retrieval
systems. In this regard, we introduce the Transformer Encoder Reasoning Network
(TERN), an architecture built upon one of the modern relationship-aware
self-attentive architectures, the Transformer Encoder (TE). This architecture
is able to separately reason on the two different modalities and to enforce a
final common abstract concept space by sharing the weights of the deeper
transformer layers. Thanks to this design, the implemented network is able to
produce compact and very rich visual and textual features available for the
successive indexing step. Experiments are conducted on the MS-COCO dataset, and
we evaluate the results using a discounted cumulative gain metric with
relevance computed exploiting caption similarities, in order to assess possibly
non-exact but relevant search results. We demonstrate that on this metric we
are able to achieve state-of-the-art results in the image retrieval task. Our
code is freely available at https://github.com/mesnico/TERN.
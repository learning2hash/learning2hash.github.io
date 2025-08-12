---
layout: publication
title: Zero-shot Composed Image Retrieval Considering Query-target Relationship Leveraging
  Masked Image-text Pairs
authors: Huaying Zhang, Rintaro Yanagi, Ren Togo, Takahiro Ogawa, Miki Haseyama
conference: 2024 IEEE International Conference on Image Processing (ICIP)
year: 2024
bibkey: zhang2024zero
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.18836'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Zhang et al.
---
This paper proposes a novel zero-shot composed image retrieval (CIR) method
considering the query-target relationship by masked image-text pairs. The
objective of CIR is to retrieve the target image using a query image and a
query text. Existing methods use a textual inversion network to convert the
query image into a pseudo word to compose the image and text and use a
pre-trained visual-language model to realize the retrieval. However, they do
not consider the query-target relationship to train the textual inversion
network to acquire information for retrieval. In this paper, we propose a novel
zero-shot CIR method that is trained end-to-end using masked image-text pairs.
By exploiting the abundant image-text pairs that are convenient to obtain with
a masking strategy for learning the query-target relationship, it is expected
that accurate zero-shot CIR using a retrieval-focused textual inversion network
can be realized. Experimental results show the effectiveness of the proposed
method.
---
layout: publication
title: A New Fine-grained Alignment Method For Image-text Matching
authors: Yang Zhang
conference: Arxiv
year: 2023
bibkey: zhang2023new
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.02183'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Yang Zhang
---
Image-text retrieval is a widely studied topic in the field of computer
vision due to the exponential growth of multimedia data, whose core concept is
to measure the similarity between images and text. However, most existing
retrieval methods heavily rely on cross-attention mechanisms for cross-modal
fine-grained alignment, which takes into account excessive irrelevant regions
and treats prominent and non-significant words equally, thereby limiting
retrieval accuracy. This paper aims to investigate an alignment approach that
reduces the involvement of non-significant fragments in images and text while
enhancing the alignment of prominent segments. For this purpose, we introduce
the Cross-Modal Prominent Fragments Enhancement Aligning Network(CPFEAN), which
achieves improved retrieval accuracy by diminishing the participation of
irrelevant regions during alignment and relatively increasing the alignment
similarity of prominent words. Additionally, we incorporate prior textual
information into image regions to reduce misalignment occurrences. In practice,
we first design a novel intra-modal fragments relationship reasoning method,
and subsequently employ our proposed alignment mechanism to compute the
similarity between images and text. Extensive quantitative comparative
experiments on MS-COCO and Flickr30K datasets demonstrate that our approach
outperforms state-of-the-art methods by about 5% to 10% in the rSum metric.
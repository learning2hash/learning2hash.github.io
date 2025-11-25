---
layout: publication
title: 'Transcending Fusion: A Multi-scale Alignment Method For Remote Sensing Image-text
  Retrieval'
authors: Rui Yang, Shuang Wang, Yingping Han, Yuanheng Li, Dong Zhao, Dou Quan, Yanhe
  Guo, Licheng Jiao
conference: Arxiv
year: 2024
bibkey: yang2024transcending
citations: 0
additional_links: [{name: Code, url: 'https://github.com/yr666666/MSA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2405.18959'}]
tags: ["Multimodal Retrieval", "Text Retrieval"]
short_authors: Yang et al.
---
Remote Sensing Image-Text Retrieval (RSITR) is pivotal for knowledge services
and data mining in the remote sensing (RS) domain. Considering the multi-scale
representations in image content and text vocabulary can enable the models to
learn richer representations and enhance retrieval. Current multi-scale RSITR
approaches typically align multi-scale fused image features with text features,
but overlook aligning image-text pairs at distinct scales separately. This
oversight restricts their ability to learn joint representations suitable for
effective retrieval. We introduce a novel Multi-Scale Alignment (MSA) method to
overcome this limitation. Our method comprises three key innovations: (1)
Multi-scale Cross-Modal Alignment Transformer (MSCMAT), which computes
cross-attention between single-scale image features and localized text
features, integrating global textual context to derive a matching score matrix
within a mini-batch, (2) a multi-scale cross-modal semantic alignment loss that
enforces semantic alignment across scales, and (3) a cross-scale multi-modal
semantic consistency loss that uses the matching matrix from the largest scale
to guide alignment at smaller scales. We evaluated our method across multiple
datasets, demonstrating its efficacy with various visual backbones and
establishing its superiority over existing state-of-the-art methods. The GitHub
URL for our project is: https://github.com/yr666666/MSA
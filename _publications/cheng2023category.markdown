---
layout: publication
title: Category-oriented Representation Learning For Image To Multi-modal Retrieval
authors: Zida Cheng, Chen Ju, Shuai Xiao, Xu Chen, Zhonghua Zhai, Xiaoyi Zeng, Weilin
  Huang, Junchi Yan
conference: Arxiv
year: 2023
bibkey: cheng2023category
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03972'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Scalability"]
short_authors: Cheng et al.
---
The rise of multi-modal search requests from users has highlighted the
importance of multi-modal retrieval (i.e. image-to-text or text-to-image
retrieval), yet the more complex task of image-to-multi-modal retrieval,
crucial for many industry applications, remains under-explored. To address this
gap and promote further research, we introduce and define the concept of
Image-to-Multi-Modal Retrieval (IMMR), a process designed to retrieve rich
multi-modal (i.e. image and text) documents based on image queries. We focus on
representation learning for IMMR and analyze three key challenges for it: 1)
skewed data and noisy label in real-world industrial data, 2) the
information-inequality between image and text modality of documents when
learning representations, 3) effective and efficient training in large-scale
industrial contexts. To tackle the above challenges, we propose a novel
framework named organizing categories and learning by classification for
retrieval (OCLEAR). It consists of three components: 1) a novel
category-oriented data governance scheme coupled with a large-scale
classification-based learning paradigm, which handles the skewed and noisy data
from a data perspective. 2) model architecture specially designed for
multi-modal learning, where information-inequality between image and text
modality of documents is considered for modality fusion. 3) a hybrid parallel
training approach for tackling large-scale training in industrial scenario. The
proposed framework achieves SOTA performance on public datasets and has been
deployed in a real-world industrial e-commence system, leading to significant
business growth. Code will be made publicly available.
---
layout: publication
title: Dual-level Cross-modal Contrastive Clustering
authors: Haixin Zhang, Yongjun Li, Dong Huang
conference: Arxiv
year: 2024
bibkey: zhang2024dual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.04561'}]
tags: []
short_authors: Haixin Zhang, Yongjun Li, Dong Huang
---
Image clustering, which involves grouping images into different clusters
without labels, is a key task in unsupervised learning. Although previous deep
clustering methods have achieved remarkable results, they only explore the
intrinsic information of the image itself but overlook external supervision
knowledge to improve the semantic understanding of images. Recently,
visual-language pre-trained model on large-scale datasets have been used in
various downstream tasks and have achieved great results. However, there is a
gap between visual representation learning and textual semantic learning, and
how to properly utilize the representation of two different modalities for
clustering is still a big challenge. To tackle the challenges, we propose a
novel image clustering framwork, named Dual-level Cross-Modal Contrastive
Clustering (DXMC). Firstly, external textual information is introduced for
constructing a semantic space which is adopted to generate image-text pairs.
Secondly, the image-text pairs are respectively sent to pre-trained image and
text encoder to obtain image and text embeddings which subsquently are fed into
four well-designed networks. Thirdly, dual-level cross-modal contrastive
learning is conducted between discriminative representations of different
modalities and distinct level. Extensive experimental results on five benchmark
datasets demonstrate the superiority of our proposed method.
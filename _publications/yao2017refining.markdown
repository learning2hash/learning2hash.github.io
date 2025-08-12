---
layout: publication
title: Refining Image Categorization By Exploiting Web Images And General Corpus
authors: Yazhou Yao, Jian Zhang, Fumin Shen, Xiansheng Hua, Wankou Yang, Zhenmin Tang
conference: Arxiv
year: 2017
bibkey: yao2017refining
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.05451'}]
tags: []
short_authors: Yao et al.
---
Studies show that refining real-world categories into semantic subcategories
contributes to better image modeling and classification. Previous image
sub-categorization work relying on labeled images and WordNet's hierarchy is
not only labor-intensive, but also restricted to classify images into NOUN
subcategories. To tackle these problems, in this work, we exploit general
corpus information to automatically select and subsequently classify web images
into semantic rich (sub-)categories. The following two major challenges are
well studied: 1) noise in the labels of subcategories derived from the general
corpus; 2) noise in the labels of images retrieved from the web. Specifically,
we first obtain the semantic refinement subcategories from the text perspective
and remove the noise by the relevance-based approach. To suppress the search
error induced noisy images, we then formulate image selection and classifier
learning as a multi-class multi-instance learning problem and propose to solve
the employed problem by the cutting-plane algorithm. The experiments show
significant performance gains by using the generated data of our way on both
image categorization and sub-categorization tasks. The proposed approach also
consistently outperforms existing weakly supervised and web-supervised
approaches.
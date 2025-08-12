---
layout: publication
title: 'Focusing On Persons: Colorizing Old Images Learning From Modern Historical
  Movies'
authors: Xin Jin, Zhonglan Li, Ke Liu, Dongqing Zou, Xiaodong Li, Xingfan Zhu, Ziyin
  Zhou, Qilong Sun, Qingyu Liu
conference: Arxiv
year: 2021
bibkey: jin2021focusing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.06515'}]
tags: ["Datasets"]
short_authors: Jin et al.
---
In industry, there exist plenty of scenarios where old gray photos need to be
automatically colored, such as video sites and archives. In this paper, we
present the HistoryNet focusing on historical person's diverse high fidelity
clothing colorization based on fine grained semantic understanding and prior.
Colorization of historical persons is realistic and practical, however,
existing methods do not perform well in the regards. In this paper, a
HistoryNet including three parts, namely, classification, fine grained semantic
parsing and colorization, is proposed. Classification sub-module supplies
classifying of images according to the eras, nationalities and garment types;
Parsing sub-network supplies the semantic for person contours, clothing and
background in the image to achieve more accurate colorization of clothes and
persons and prevent color overflow. In the training process, we integrate
classification and semantic parsing features into the coloring generation
network to improve colorization. Through the design of classification and
parsing subnetwork, the accuracy of image colorization can be improved and the
boundary of each part of image can be more clearly. Moreover, we also propose a
novel Modern Historical Movies Dataset (MHMD) containing 1,353,166 images and
42 labels of eras, nationalities, and garment types for automatic colorization
from 147 historical movies or TV series made in modern time. Various
quantitative and qualitative comparisons demonstrate that our method
outperforms the state-of-the-art colorization methods, especially on military
uniforms, which has correct colors according to the historical literatures.
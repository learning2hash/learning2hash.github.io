---
layout: publication
title: Multimodal Neural Machine Translation With Search Engine Based Image Retrieval
authors: Zhenhao Tang, Xiaobing Zhang, Zi Long, Xianghua Fu
conference: Arxiv
year: 2022
bibkey: tang2022multimodal
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.00767'}]
tags: ["Image Retrieval"]
short_authors: Tang et al.
---
Recently, numbers of works shows that the performance of neural machine
translation (NMT) can be improved to a certain extent with using visual
information. However, most of these conclusions are drawn from the analysis of
experimental results based on a limited set of bilingual sentence-image pairs,
such as Multi30K. In these kinds of datasets, the content of one bilingual
parallel sentence pair must be well represented by a manually annotated image,
which is different with the actual translation situation. Some previous works
are proposed to addressed the problem by retrieving images from exiting
sentence-image pairs with topic model. However, because of the limited
collection of sentence-image pairs they used, their image retrieval method is
difficult to deal with the out-of-vocabulary words, and can hardly prove that
visual information enhance NMT rather than the co-occurrence of images and
sentences. In this paper, we propose an open-vocabulary image retrieval methods
to collect descriptive images for bilingual parallel corpus using image search
engine. Next, we propose text-aware attentive visual encoder to filter
incorrectly collected noise images. Experiment results on Multi30K and other
two translation datasets show that our proposed method achieves significant
improvements over strong baselines.
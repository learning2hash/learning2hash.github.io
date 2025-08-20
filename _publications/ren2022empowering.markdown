---
layout: publication
title: Empowering Dual-encoder With Query Generator For Cross-lingual Dense Retrieval
authors: Houxing Ren, Linjun Shou, Ning Wu, Ming Gong, Daxin Jiang
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: ren2022empowering
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.14991'}]
tags: [Evaluation, Datasets, EMNLP]
short_authors: Ren et al.
---
In monolingual dense retrieval, lots of works focus on how to distill
knowledge from cross-encoder re-ranker to dual-encoder retriever and these
methods achieve better performance due to the effectiveness of cross-encoder
re-ranker. However, we find that the performance of the cross-encoder re-ranker
is heavily influenced by the number of training samples and the quality of
negative samples, which is hard to obtain in the cross-lingual setting. In this
paper, we propose to use a query generator as the teacher in the cross-lingual
setting, which is less dependent on enough training samples and high-quality
negative samples. In addition to traditional knowledge distillation, we further
propose a novel enhancement method, which uses the query generator to help the
dual-encoder align queries from different languages, but does not need any
additional parallel sentences. The experimental results show that our method
outperforms the state-of-the-art methods on two benchmark datasets.
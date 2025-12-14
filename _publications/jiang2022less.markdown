---
layout: publication
title: 'Less Is More: Parameter-free Text Classification With Gzip'
authors: Zhiying Jiang, Matthew Y. R. Yang, Mikhail Tsirlin, Raphael Tang, Jimmy Lin
conference: Arxiv
year: 2022
bibkey: jiang2022less
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.09410'}]
tags: [Few-shot & Zero-shot, Neural Hashing, Datasets]
short_authors: Jiang et al.
---
Deep neural networks (DNNs) are often used for text classification tasks as
they usually achieve high levels of accuracy. However, DNNs can be
computationally intensive with billions of parameters and large amounts of
labeled data, which can make them expensive to use, to optimize and to transfer
to out-of-distribution (OOD) cases in practice. In this paper, we propose a
non-parametric alternative to DNNs that's easy, light-weight and universal in
text classification: a combination of a simple compressor like gzip with a
\(k\)-nearest-neighbor classifier. Without any training, pre-training or
fine-tuning, our method achieves results that are competitive with
non-pretrained deep learning methods on six in-distributed datasets. It even
outperforms BERT on all five OOD datasets, including four low-resource
languages. Our method also performs particularly well in few-shot settings
where labeled data are too scarce for DNNs to achieve a satisfying accuracy.
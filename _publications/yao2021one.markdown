---
layout: publication
title: One-shot Key Information Extraction From Document With Deep Partial Graph Matching
authors: Minghong Yao, Zhiguang Liu, Liangwei Wang, Houqiang Li, Liansheng Zhuang
conference: Arxiv
year: 2021
bibkey: yao2021one
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.13967'}]
tags: []
short_authors: Yao et al.
---
Automating the Key Information Extraction (KIE) from documents improves
efficiency, productivity, and security in many industrial scenarios such as
rapid indexing and archiving. Many existing supervised learning methods for the
KIE task need to feed a large number of labeled samples and learn separate
models for different types of documents. However, collecting and labeling a
large dataset is time-consuming and is not a user-friendly requirement for many
cloud platforms. To overcome these challenges, we propose a deep end-to-end
trainable network for one-shot KIE using partial graph matching. Contrary to
previous methods that the learning of similarity and solving are optimized
separately, our method enables the learning of the two processes in an
end-to-end framework. Existing one-shot KIE methods are either template or
simple attention-based learning approach that struggle to handle texts that are
shifted beyond their desired positions caused by printers, as illustrated in
Fig.1. To solve this problem, we add one-to-(at most)-one constraint such that
we will find the globally optimized solution even if some texts are drifted.
Further, we design a multimodal context ensemble block to boost the performance
through fusing features of spatial, textual, and aspect representations. To
promote research of KIE, we collected and annotated a one-shot document KIE
dataset named DKIE with diverse types of images. The DKIE dataset consists of
2.5K document images captured by mobile phones in natural scenes, and it is the
largest available one-shot KIE dataset up to now. The results of experiments on
DKIE show that our method achieved state-of-the-art performance compared with
recent one-shot and supervised learning approaches. The dataset and proposed
one-shot KIE model will be released soo
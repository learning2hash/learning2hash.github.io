---
layout: publication
title: Memory Regulation And Alignment Toward Generalizer Rgb-infrared Person
authors: Feng Chen, Fei Wu, Qi Wu, Zhiguo Wan
conference: Arxiv
year: 2021
bibkey: chen2021memory
citations: 5
additional_links: [{name: Code, url: 'https://github.com/Chenfeng1271/MGMRA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2109.08843'}]
tags: ["Distance Metric Learning", "Hashing Methods", "Robustness"]
short_authors: Chen et al.
---
The domain shift, coming from unneglectable modality gap and non-overlapped
identity classes between training and test sets, is a major issue of
RGB-Infrared person re-identification. A key to tackle the inherent issue --
domain shift -- is to enforce the data distributions of the two domains to be
similar. However, RGB-IR ReID always demands discriminative features, leading
to over-rely feature sensitivity of seen classes, \textit\{e.g.\}, via
attention-based feature alignment or metric learning. Therefore, predicting the
unseen query category from predefined training classes may not be accurate and
leads to a sub-optimal adversarial gradient. In this paper, we uncover it in a
more explainable way and propose a novel multi-granularity memory regulation
and alignment module (MG-MRA) to solve this issue. By explicitly incorporating
a latent variable attribute, from fine-grained to coarse semantic granularity,
into intermediate features, our method could alleviate the over-confidence of
the model about discriminative features of seen classes. Moreover, instead of
matching discriminative features by traversing nearest neighbor, sparse
attributes, \textit\{i.e.\}, global structural pattern, are recollected with
respect to features and assigned to measure pair-wise image similarity in
hashing. Extensive experiments on RegDB \cite\{RegDB\} and SYSU-MM01 \cite\{SYSU\}
show the superiority of the proposed method that outperforms existing
state-of-the-art methods. Our code is available in
https://github.com/Chenfeng1271/MGMRA.
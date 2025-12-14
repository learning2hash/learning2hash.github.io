---
layout: publication
title: 'Watch And Learn: Mapping Language And Noisy Real-world Videos With Self-supervision'
authors: Yujie Zhong, Linhai Xie, Sen Wang, Lucia Specia, Yishu Miao
conference: Arxiv
year: 2020
bibkey: zhong2020watch
citations: 0
additional_links: [{name: Code, url: 'https://github.com/zyj-13/WAL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2011.09634'}]
tags: [Evaluation, Supervised, Self-Supervised, Datasets, Robustness, Tools & Libraries]
short_authors: Zhong et al.
---
In this paper, we teach machines to understand visuals and natural language
by learning the mapping between sentences and noisy video snippets without
explicit annotations. Firstly, we define a self-supervised learning framework
that captures the cross-modal information. A novel adversarial learning module
is then introduced to explicitly handle the noises in the natural videos, where
the subtitle sentences are not guaranteed to be strongly corresponded to the
video snippets. For training and evaluation, we contribute a new dataset
`ApartmenTour' that contains a large number of online videos and subtitles. We
carry out experiments on the bidirectional retrieval tasks between sentences
and videos, and the results demonstrate that our proposed model achieves the
state-of-the-art performance on both retrieval tasks and exceeds several strong
baselines. The dataset can be downloaded at https://github.com/zyj-13/WAL.
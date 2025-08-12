---
layout: publication
title: 'Complementing Representation Deficiency In Few-shot Image Classification:
  A Meta-learning Approach'
authors: Xian Zhong, Cheng Gu, Wenxin Huang, Lin Li, Shuqin Chen, Chia-wen Lin
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: zhong2020complementing
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.10778'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhong et al.
---
Few-shot learning is a challenging problem that has attracted more and more
attention recently since abundant training samples are difficult to obtain in
practical applications. Meta-learning has been proposed to address this issue,
which focuses on quickly adapting a predictor as a base-learner to new tasks,
given limited labeled samples. However, a critical challenge for meta-learning
is the representation deficiency since it is hard to discover common
information from a small number of training samples or even one, as is the
representation of key features from such little information. As a result, a
meta-learner cannot be trained well in a high-dimensional parameter space to
generalize to new tasks. Existing methods mostly resort to extracting less
expressive features so as to avoid the representation deficiency. Aiming at
learning better representations, we propose a meta-learning approach with
complemented representations network (MCRNet) for few-shot image
classification. In particular, we embed a latent space, where latent codes are
reconstructed with extra representation information to complement the
representation deficiency. Furthermore, the latent space is established with
variational inference, collaborating well with different base-learners, and can
be extended to other models. Finally, our end-to-end framework achieves the
state-of-the-art performance in image classification on three standard few-shot
learning datasets.
---
layout: publication
title: 'DP-MERF: Differentially Private Mean Embeddings With Random Features For Practical
  Privacy-preserving Data Generation'
authors: Frederik Harder, Kamil Adamczewski, Mijung Park
conference: Arxiv
year: 2020
bibkey: harder2020dp
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.11603'}]
tags: []
short_authors: Frederik Harder, Kamil Adamczewski, Mijung Park
---
We propose a differentially private data generation paradigm using random
feature representations of kernel mean embeddings when comparing the
distribution of true data with that of synthetic data. We exploit the random
feature representations for two important benefits. First, we require a minimal
privacy cost for training deep generative models. This is because unlike
kernel-based distance metrics that require computing the kernel matrix on all
pairs of true and synthetic data points, we can detach the data-dependent term
from the term solely dependent on synthetic data. Hence, we need to perturb the
data-dependent term only once and then use it repeatedly during the generator
training. Second, we can obtain an analytic sensitivity of the kernel mean
embedding as the random features are norm bounded by construction. This removes
the necessity of hyper-parameter search for a clipping norm to handle the
unknown sensitivity of a generator network. We provide several variants of our
algorithm, differentially-private mean embeddings with random features
(DP-MERF) to jointly generate labels and input features for datasets such as
heterogeneous tabular data and image data. Our algorithm achieves drastically
better privacy-utility trade-offs than existing methods when tested on several
datasets.
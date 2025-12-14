---
layout: publication
title: 'RREH: Reconstruction Relations Embedded Hashing For Semi-paired Cross-modal
  Retrieval'
authors: Jianzong Wang, Haoxiang Shi, Kaiyi Luo, Xulong Zhang, Ning Cheng, Jing Xiao
conference: Lecture Notes in Computer Science
year: 2024
bibkey: wang2024rreh
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.17777'}]
tags: [Evaluation, Supervised, Efficiency, Datasets, Multimodal Retrieval, Scalability,
  Unsupervised, Tools & Libraries, Hashing Methods]
short_authors: Wang et al.
---
Known for efficient computation and easy storage, hashing has been
extensively explored in cross-modal retrieval. The majority of current hashing
models are predicated on the premise of a direct one-to-one mapping between
data points. However, in real practice, data correspondence across modalities
may be partially provided. In this research, we introduce an innovative
unsupervised hashing technique designed for semi-paired cross-modal retrieval
tasks, named Reconstruction Relations Embedded Hashing (RREH). RREH assumes
that multi-modal data share a common subspace. For paired data, RREH explores
the latent consistent information of heterogeneous modalities by seeking a
shared representation. For unpaired data, to effectively capture the latent
discriminative features, the high-order relationships between unpaired data and
anchors are embedded into the latent subspace, which are computed by efficient
linear reconstruction. The anchors are sampled from paired data, which improves
the efficiency of hash learning. The RREH trains the underlying features and
the binary encodings in a unified framework with high-order reconstruction
relations preserved. With the well devised objective function and discrete
optimization algorithm, RREH is designed to be scalable, making it suitable for
large-scale datasets and facilitating efficient cross-modal retrieval. In the
evaluation process, the proposed is tested with partially paired data to
establish its superiority over several existing methods.
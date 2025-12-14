---
layout: publication
title: Self-supervised Photographic Image Layout Representation Learning
authors: Zhaoran Zhao, Peng Lu, Xujun Peng, Wenhao Guo
conference: Arxiv
year: 2024
bibkey: zhao2024self
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.03740'}]
tags: [Evaluation, Supervised, Image Retrieval, Self-Supervised, Datasets]
short_authors: Zhao et al.
---
In the domain of image layout representation learning, the critical process
of translating image layouts into succinct vector forms is increasingly
significant across diverse applications, such as image retrieval, manipulation,
and generation. Most approaches in this area heavily rely on costly labeled
datasets and notably lack in adapting their modeling and learning methods to
the specific nuances of photographic image layouts. This shortfall makes the
learning process for photographic image layouts suboptimal. In our research, we
directly address these challenges. We innovate by defining basic layout
primitives that encapsulate various levels of layout information and by mapping
these, along with their interconnections, onto a heterogeneous graph structure.
This graph is meticulously engineered to capture the intricate layout
information within the pixel domain explicitly. Advancing further, we introduce
novel pretext tasks coupled with customized loss functions, strategically
designed for effective self-supervised learning of these layout graphs.
Building on this foundation, we develop an autoencoder-based network
architecture skilled in compressing these heterogeneous layout graphs into
precise, dimensionally-reduced layout representations. Additionally, we
introduce the LODB dataset, which features a broader range of layout categories
and richer semantics, serving as a comprehensive benchmark for evaluating the
effectiveness of layout representation learning methods. Our extensive
experimentation on this dataset demonstrates the superior performance of our
approach in the realm of photographic image layout representation learning.
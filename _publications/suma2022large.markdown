---
layout: publication
title: Large-to-small Image Resolution Asymmetry In Deep Metric Learning
authors: Pavel Suma, Giorgos Tolias
conference: Arxiv
year: 2022
bibkey: suma2022large
citations: 0
additional_links: [{name: Code, url: 'https://github.com/pavelsuma/raml'}, {name: Paper,
    url: 'https://arxiv.org/abs/2210.05463'}]
tags: [Distance Metric Learning, Image Retrieval, Evaluation, Efficiency]
short_authors: Pavel Suma, Giorgos Tolias
---
Deep metric learning for vision is trained by optimizing a representation
network to map (non-)matching image pairs to (non-)similar representations.
During testing, which typically corresponds to image retrieval, both database
and query examples are processed by the same network to obtain the
representation used for similarity estimation and ranking. In this work, we
explore an asymmetric setup by light-weight processing of the query at a small
image resolution to enable fast representation extraction. The goal is to
obtain a network for database examples that is trained to operate on large
resolution images and benefits from fine-grained image details, and a second
network for query examples that operates on small resolution images but
preserves a representation space aligned with that of the database network. We
achieve this with a distillation approach that transfers knowledge from a fixed
teacher network to a student via a loss that operates per image and solely
relies on coupled augmentations without the use of any labels. In contrast to
prior work that explores such asymmetry from the point of view of different
network architectures, this work uses the same architecture but modifies the
image resolution. We conclude that resolution asymmetry is a better way to
optimize the performance/efficiency trade-off than architecture asymmetry.
Evaluation is performed on three standard deep metric learning benchmarks,
namely CUB200, Cars196, and SOP. Code: https://github.com/pavelsuma/raml
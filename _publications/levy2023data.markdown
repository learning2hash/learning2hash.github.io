---
layout: publication
title: Data Roaming And Quality Assessment For Composed Image Retrieval
authors: Matan Levy, Rami Ben-ari, Nir Darshan, Dani Lischinski
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: levy2023data
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09429'}]
tags: ["AAAI", "Image Retrieval"]
short_authors: Levy et al.
---
The task of Composed Image Retrieval (CoIR) involves queries that combine
image and text modalities, allowing users to express their intent more
effectively. However, current CoIR datasets are orders of magnitude smaller
compared to other vision and language (V&L) datasets. Additionally, some of
these datasets have noticeable issues, such as queries containing redundant
modalities. To address these shortcomings, we introduce the Large Scale
Composed Image Retrieval (LaSCo) dataset, a new CoIR dataset which is ten times
larger than existing ones. Pre-training on our LaSCo, shows a noteworthy
improvement in performance, even in zero-shot. Furthermore, we propose a new
approach for analyzing CoIR datasets and methods, which detects modality
redundancy or necessity, in queries. We also introduce a new CoIR baseline, the
Cross-Attention driven Shift Encoder (CASE). This baseline allows for early
fusion of modalities using a cross-attention module and employs an additional
auxiliary task during training. Our experiments demonstrate that this new
baseline outperforms the current state-of-the-art methods on established
benchmarks like FashionIQ and CIRR.
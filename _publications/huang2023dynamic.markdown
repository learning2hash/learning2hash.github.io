---
layout: publication
title: Dynamic Weighted Combiner For Mixed-modal Image Retrieval
authors: Fuxiang Huang, Lei Zhang, Xiaowei Fu, Suqi Song
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: huang2023dynamic
citations: 4
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2312.06179'}]
tags: ["AAAI", "Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Huang et al.
---
Mixed-Modal Image Retrieval (MMIR) as a flexible search paradigm has
attracted wide attention. However, previous approaches always achieve limited
performance, due to two critical factors are seriously overlooked. 1) The
contribution of image and text modalities is different, but incorrectly treated
equally. 2) There exist inherent labeling noises in describing users'
intentions with text in web datasets from diverse real-world scenarios, giving
rise to overfitting. We propose a Dynamic Weighted Combiner (DWC) to tackle the
above challenges, which includes three merits. First, we propose an Editable
Modality De-equalizer (EMD) by taking into account the contribution disparity
between modalities, containing two modality feature editors and an adaptive
weighted combiner. Second, to alleviate labeling noises and data bias, we
propose a dynamic soft-similarity label generator (SSG) to implicitly improve
noisy supervision. Finally, to bridge modality gaps and facilitate similarity
learning, we propose a CLIP-based mutual enhancement module alternately trained
by a mixed-modality contrastive loss. Extensive experiments verify that our
proposed model significantly outperforms state-of-the-art methods on real-world
datasets. The source code is available at
https://github.com/fuxianghuang1/DWC.
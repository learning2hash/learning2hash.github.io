---
layout: publication
title: Retrieval-guided Cross-view Image Synthesis
authors: Hongji Yang, Yiru Li, Yingying Zhu
conference: Arxiv
year: 2024
bibkey: yang2024retrieval
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.19510'}]
tags: [Self-Supervised, Tools & Libraries, Datasets]
short_authors: Hongji Yang, Yiru Li, Yingying Zhu
---
Information retrieval techniques have demonstrated exceptional capabilities
in identifying semantic similarities across diverse domains through robust
feature representations. However, their potential in guiding synthesis tasks,
particularly cross-view image synthesis, remains underexplored. Cross-view
image synthesis presents significant challenges in establishing reliable
correspondences between drastically different viewpoints. To address this, we
propose a novel retrieval-guided framework that reimagines how retrieval
techniques can facilitate effective cross-view image synthesis. Unlike existing
methods that rely on auxiliary information, such as semantic segmentation maps
or preprocessing modules, our retrieval-guided framework captures semantic
similarities across different viewpoints, trained through contrastive learning
to create a smooth embedding space. Furthermore, a novel fusion mechanism
leverages these embeddings to guide image synthesis while learning and encoding
both view-invariant and view-specific features. To further advance this area,
we introduce VIGOR-GEN, a new urban-focused dataset with complex viewpoint
variations in real-world scenarios. Extensive experiments demonstrate that our
retrieval-guided approach significantly outperforms existing methods on the
CVUSA, CVACT and VIGOR-GEN datasets, particularly in retrieval accuracy (R@1)
and synthesis quality (FID). Our work bridges information retrieval and
synthesis tasks, offering insights into how retrieval techniques can address
complex cross-domain synthesis challenges.
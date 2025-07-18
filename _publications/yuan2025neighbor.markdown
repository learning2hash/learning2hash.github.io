---
layout: publication
title: Neighbor-based Feature And Index Enhancement For Person Re-identification
authors: Yuan Chao, Zhang Tianyi, Niu Guanglin
conference: Expert Systems with Applications
year: 2025
bibkey: yuan2025neighbor
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.11798'}]
tags: [DATASETS, Evaluation, Robustness]
---
Person re-identification (Re-ID) aims to match the same pedestrian in a large
gallery with different cameras and views. Enhancing the robustness of the
extracted feature representations is a main challenge in Re-ID. Existing
methods usually improve feature representation by improving model architecture,
but most methods ignore the potential contextual information, which limits the
effectiveness of feature representation and retrieval performance. Neighborhood
information, especially the potential information of multi-order neighborhoods,
can effectively enrich feature expression and improve retrieval accuracy, but
this has not been fully explored in existing research. Therefore, we propose a
novel model DMON-ARO that leverages latent neighborhood information to enhance
both feature representation and index performance. Our approach is built on two
complementary modules: Dynamic Multi-Order Neighbor Modeling (DMON) and
Asymmetric Relationship Optimization (ARO). The DMON module dynamically
aggregates multi-order neighbor relationships, allowing it to capture richer
contextual information and enhance feature representation through adaptive
neighborhood modeling. Meanwhile, ARO refines the distance matrix by optimizing
query-to-gallery relationships, improving the index accuracy. Extensive
experiments on three benchmark datasets demonstrate that our approach achieves
performance improvements against baseline models, which illustrate the
effectiveness of our model. Specifically, our model demonstrates improvements
in Rank-1 accuracy and mAP. Moreover, this method can also be directly extended
to other re-identification tasks.
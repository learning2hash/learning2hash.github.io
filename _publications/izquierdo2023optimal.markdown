---
layout: publication
title: Optimal Transport Aggregation For Visual Place Recognition
authors: Sergio Izquierdo, Javier Civera
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: izquierdo2023optimal
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.15937'}]
tags: ["CVPR", "Datasets", "Hybrid ANN Methods", "Re-Ranking"]
short_authors: Sergio Izquierdo, Javier Civera
---
The task of Visual Place Recognition (VPR) aims to match a query image
against references from an extensive database of images from different places,
relying solely on visual cues. State-of-the-art pipelines focus on the
aggregation of features extracted from a deep backbone, in order to form a
global descriptor for each image. In this context, we introduce SALAD (Sinkhorn
Algorithm for Locally Aggregated Descriptors), which reformulates NetVLAD's
soft-assignment of local features to clusters as an optimal transport problem.
In SALAD, we consider both feature-to-cluster and cluster-to-feature relations
and we also introduce a 'dustbin' cluster, designed to selectively discard
features deemed non-informative, enhancing the overall descriptor quality.
Additionally, we leverage and fine-tune DINOv2 as a backbone, which provides
enhanced description power for the local features, and dramatically reduces the
required training time. As a result, our single-stage method not only surpasses
single-stage baselines in public VPR datasets, but also surpasses two-stage
methods that add a re-ranking with significantly higher cost. Code and models
are available at https://github.com/serizba/salad.
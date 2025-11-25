---
layout: publication
title: 'Beyond Supervised Vs. Unsupervised: Representative Benchmarking And Analysis
  Of Image Representation Learning'
authors: Matthew Gwilliam, Abhinav Shrivastava
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: gwilliam2022beyond
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.08347'}]
tags: ["CVPR", "Evaluation", "Self-Supervised", "Unsupervised"]
short_authors: Matthew Gwilliam, Abhinav Shrivastava
---
By leveraging contrastive learning, clustering, and other pretext tasks,
unsupervised methods for learning image representations have reached impressive
results on standard benchmarks. The result has been a crowded field - many
methods with substantially different implementations yield results that seem
nearly identical on popular benchmarks, such as linear evaluation on ImageNet.
However, a single result does not tell the whole story. In this paper, we
compare methods using performance-based benchmarks such as linear evaluation,
nearest neighbor classification, and clustering for several different datasets,
demonstrating the lack of a clear front-runner within the current
state-of-the-art. In contrast to prior work that performs only supervised vs.
unsupervised comparison, we compare several different unsupervised methods
against each other. To enrich this comparison, we analyze embeddings with
measurements such as uniformity, tolerance, and centered kernel alignment
(CKA), and propose two new metrics of our own: nearest neighbor graph
similarity and linear prediction overlap. We reveal through our analysis that
in isolation, single popular methods should not be treated as though they
represent the field as a whole, and that future work ought to consider how to
leverage the complimentary nature of these methods. We also leverage CKA to
provide a framework to robustly quantify augmentation invariance, and provide a
reminder that certain types of invariance will be undesirable for downstream
tasks.
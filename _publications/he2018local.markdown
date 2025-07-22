---
layout: publication
title: Local Descriptors Optimized For Average Precision
authors: He Kun, Lu Yan, Sclaroff Stan
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: he2018local
citations: 209
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.05312'}]
tags: ["CVPR", "Evaluation"]
short_authors: He Kun, Lu Yan, Sclaroff Stan
---
Extraction of local feature descriptors is a vital stage in the solution
pipelines for numerous computer vision tasks. Learning-based approaches improve
performance in certain tasks, but still cannot replace handcrafted features in
general. In this paper, we improve the learning of local feature descriptors by
optimizing the performance of descriptor matching, which is a common stage that
follows descriptor extraction in local feature based pipelines, and can be
formulated as nearest neighbor retrieval. Specifically, we directly optimize a
ranking-based retrieval performance metric, Average Precision, using deep
neural networks. This general-purpose solution can also be viewed as a listwise
learning to rank approach, which is advantageous compared to recent local
ranking approaches. On standard benchmarks, descriptors learned with our
formulation achieve state-of-the-art results in patch verification, patch
retrieval, and image matching.
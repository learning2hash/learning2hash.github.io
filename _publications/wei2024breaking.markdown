---
layout: publication
title: 'Breaking The Frame: Visual Place Recognition By Overlap Prediction'
authors: Tong Wei, Philipp Lindenberger, Jiri Matas, Daniel Barath
conference: Arxiv
year: 2024
bibkey: wei2024breaking
citations: 1
additional_links: [{name: Code, url: 'https://github.com/weitong8591/vop.git'}, {
    name: Paper, url: 'https://arxiv.org/abs/2406.16204'}]
tags: ["Image Retrieval", "Scalability"]
short_authors: Wei et al.
---
Visual place recognition methods struggle with occlusions and partial visual
overlaps. We propose a novel visual place recognition approach based on overlap
prediction, called VOP, shifting from traditional reliance on global image
similarities and local features to image overlap prediction. VOP proceeds
co-visible image sections by obtaining patch-level embeddings using a Vision
Transformer backbone and establishing patch-to-patch correspondences without
requiring expensive feature detection and matching. Our approach uses a voting
mechanism to assess overlap scores for potential database images. It provides a
nuanced image retrieval metric in challenging scenarios. Experimental results
show that VOP leads to more accurate relative pose estimation and localization
results on the retrieved image pairs than state-of-the-art baselines on a
number of large-scale, real-world indoor and outdoor benchmarks. The code is
available at https://github.com/weitong8591/vop.git.
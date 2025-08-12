---
layout: publication
title: Simple Multi-dataset Detection
authors: "Xingyi Zhou, Vladlen Koltun, Philipp Kr\xE4henb\xFChl"
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: zhou2021simple
citations: 63
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.13086'}]
tags: ["CVPR", "Datasets"]
short_authors: "Xingyi Zhou, Vladlen Koltun, Philipp Kr\xE4henb\xFChl"
---
How do we build a general and broad object detection system? We use all
labels of all concepts ever annotated. These labels span diverse datasets with
potentially inconsistent taxonomies. In this paper, we present a simple method
for training a unified detector on multiple large-scale datasets. We use
dataset-specific training protocols and losses, but share a common detection
architecture with dataset-specific outputs. We show how to automatically
integrate these dataset-specific outputs into a common semantic taxonomy. In
contrast to prior work, our approach does not require manual taxonomy
reconciliation. Experiments show our learned taxonomy outperforms a
expert-designed taxonomy in all datasets. Our multi-dataset detector performs
as well as dataset-specific models on each training domain, and can generalize
to new unseen dataset without fine-tuning on them. Code is available at
https://github.com/xingyizhou/UniDet.
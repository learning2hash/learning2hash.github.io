---
layout: publication
title: 'HAMIL: Hierarchical Aggregation-based Multi-instance Learning For Microscopy
  Image Classification'
authors: Yanlun Tu, Houchao Lei, Wei Long, Yang Yang
conference: Pattern Recognition
year: 2022
bibkey: tu2021hamil
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.09764'}]
tags: ["Evaluation"]
short_authors: Tu et al.
---
Multi-instance learning is common for computer vision tasks, especially in
biomedical image processing. Traditional methods for multi-instance learning
focus on designing feature aggregation methods and multi-instance classifiers,
where the aggregation operation is performed either in feature extraction or
learning phase. As deep neural networks (DNNs) achieve great success in image
processing via automatic feature learning, certain feature aggregation
mechanisms need to be incorporated into common DNN architecture for
multi-instance learning. Moreover, flexibility and reliability are crucial
considerations to deal with varying quality and number of instances.
  In this study, we propose a hierarchical aggregation network for
multi-instance learning, called HAMIL. The hierarchical aggregation protocol
enables feature fusion in a defined order, and the simple convolutional
aggregation units lead to an efficient and flexible architecture. We assess the
model performance on two microscopy image classification tasks, namely protein
subcellular localization using immunofluorescence images and gene annotation
using spatial gene expression images. The experimental results show that HAMIL
outperforms the state-of-the-art feature aggregation methods and the existing
models for addressing these two tasks. The visualization analyses also
demonstrate the ability of HAMIL to focus on high-quality instances.
---
layout: publication
title: Multi-layered Semantic Representation Network For Multi-label Image Classification
authors: Xiwen Qu, Hao Che, Jun Huang, Linchuan Xu, Xiao Zheng
conference: International Journal of Machine Learning and Cybernetics
year: 2023
bibkey: qu2021multi
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.11596'}]
tags: ["Datasets", "Evaluation"]
short_authors: Qu et al.
---
Multi-label image classification (MLIC) is a fundamental and practical task,
which aims to assign multiple possible labels to an image. In recent years,
many deep convolutional neural network (CNN) based approaches have been
proposed which model label correlations to discover semantics of labels and
learn semantic representations of images. This paper advances this research
direction by improving both the modeling of label correlations and the learning
of semantic representations. On the one hand, besides the local semantics of
each label, we propose to further explore global semantics shared by multiple
labels. On the other hand, existing approaches mainly learn the semantic
representations at the last convolutional layer of a CNN. But it has been noted
that the image representations of different layers of CNN capture different
levels or scales of features and have different discriminative abilities. We
thus propose to learn semantic representations at multiple convolutional
layers. To this end, this paper designs a Multi-layered Semantic Representation
Network (MSRN) which discovers both local and global semantics of labels
through modeling label correlations and utilizes the label semantics to guide
the semantic representations learning at multiple layers through an attention
mechanism. Extensive experiments on four benchmark datasets including VOC 2007,
COCO, NUS-WIDE, and Apparel show a competitive performance of the proposed MSRN
against state-of-the-art models.
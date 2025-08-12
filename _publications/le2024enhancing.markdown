---
layout: publication
title: Enhancing Fine-grained Image Classification Through Attentive Batch Training
authors: Duy M. Le, Bao Q. Bui, Anh Tran, Cong Tran, Cuong Pham
conference: Arxiv
year: 2024
bibkey: le2024enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.19606'}]
tags: []
short_authors: Le et al.
---
Fine-grained image classification, which is a challenging task in computer
vision, requires precise differentiation among visually similar object
categories. In this paper, we propose 1) a novel module called Residual
Relationship Attention (RRA) that leverages the relationships between images
within each training batch to effectively integrate visual feature vectors of
batch images and 2) a novel technique called Relationship Position Encoding
(RPE), which encodes the positions of relationships between original images in
a batch and effectively preserves the relationship information between images
within the batch. Additionally, we design a novel framework, namely
Relationship Batch Integration (RBI), which utilizes RRA in conjunction with
RPE, allowing the discernment of vital visual features that may remain elusive
when examining a singular image representative of a particular class. Through
extensive experiments, our proposed method demonstrates significant
improvements in the accuracy of different fine-grained classifiers, with an
average increase of \((+2.78%)\) and \((+3.83%)\) on the CUB200-2011 and Stanford
Dog datasets, respectively, while achieving a state-of-the-art results
\((95.79%)\) on the Stanford Dog dataset. Despite not achieving the same level
of improvement as in fine-grained image classification, our method still
demonstrates its prowess in leveraging general image classification by
attaining a state-of-the-art result of \((93.71%)\) on the Tiny-Imagenet
dataset. Furthermore, our method serves as a plug-in refinement module and can
be easily integrated into different networks.
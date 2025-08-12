---
layout: publication
title: The Imaterialist Fashion Attribute Dataset
authors: Sheng Guo, Weilin Huang, Xiao Zhang, Prasanna Srikhanta, Yin Cui, Yuan Li,
  Matthew R. Scott, Hartwig Adam, Serge Belongie
conference: 2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)
year: 2019
bibkey: guo2019imaterialist
citations: 77
additional_links: [{name: Code, url: 'https://github.com/visipedia/imat_fashion_comp'},
  {name: Paper, url: 'https://arxiv.org/abs/1906.05750'}]
tags: ["Datasets", "ICCV"]
short_authors: Guo et al.
---
Large-scale image databases such as ImageNet have significantly advanced
image classification and other visual recognition tasks. However much of these
datasets are constructed only for single-label and coarse object-level
classification. For real-world applications, multiple labels and fine-grained
categories are often needed, yet very few such datasets exist publicly,
especially those of large-scale and high quality. In this work, we contribute
to the community a new dataset called iMaterialist Fashion Attribute
(iFashion-Attribute) to address this problem in the fashion domain. The dataset
is constructed from over one million fashion images with a label space that
includes 8 groups of 228 fine-grained attributes in total. Each image is
annotated by experts with multiple, high-quality fashion attributes. The result
is the first known million-scale multi-label and fine-grained image dataset. We
conduct extensive experiments and provide baseline results with modern deep
Convolutional Neural Networks (CNNs). Additionally, we demonstrate models
pre-trained on iFashion-Attribute achieve superior transfer learning
performance on fashion related tasks compared with pre-training from ImageNet
or other fashion datasets. Data is available at:
https://github.com/visipedia/imat_fashion_comp
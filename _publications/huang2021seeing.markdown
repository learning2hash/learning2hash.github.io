---
layout: publication
title: 'Seeing Out Of The Box: End-to-end Pre-training For Vision-language Representation
  Learning'
authors: Zhicheng Huang, Zhaoyang Zeng, Yupan Huang, Bei Liu, Dongmei Fu, Jianlong
  Fu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: huang2021seeing
citations: 205
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.03135'}]
tags: [Text Retrieval, CVPR]
short_authors: Huang et al.
---
We study joint learning of Convolutional Neural Network (CNN) and Transformer
for vision-language pre-training (VLPT) which aims to learn cross-modal
alignments from millions of image-text pairs. State-of-the-art approaches
extract salient image regions and align regions with words step-by-step. As
region-based visual features usually represent parts of an image, it is
challenging for existing vision-language models to fully understand the
semantics from paired natural languages. In this paper, we propose SOHO to "See
Out of tHe bOx" that takes a whole image as input, and learns vision-language
representation in an end-to-end manner. SOHO does not require bounding box
annotations which enables inference 10 times faster than region-based
approaches. In particular, SOHO learns to extract comprehensive yet compact
image features through a visual dictionary (VD) that facilitates cross-modal
understanding. VD is designed to represent consistent visual abstractions of
similar semantics. It is updated on-the-fly and utilized in our proposed
pre-training task Masked Visual Modeling (MVM). We conduct experiments on four
well-established vision-language tasks by following standard VLPT settings. In
particular, SOHO achieves absolute gains of 2.0% R@1 score on MSCOCO text
retrieval 5k test split, 1.5% accuracy on NLVR\(^2\) test-P split, 6.7% accuracy
on SNLI-VE test split, respectively.
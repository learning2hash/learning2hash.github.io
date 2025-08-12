---
layout: publication
title: Few-shot Semantic Segmentation Via Mask Aggregation
authors: Wei Ao, Shunyi Zheng, Yan Meng
conference: Neural Processing Letters
year: 2024
bibkey: ao2022few
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.07231'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Wei Ao, Shunyi Zheng, Yan Meng
---
Few-shot semantic segmentation aims to recognize novel classes with only very
few labelled data. This challenging task requires mining of the relevant
relationships between the query image and the support images. Previous works
have typically regarded it as a pixel-wise classification problem. Therefore,
various models have been designed to explore the correlation of pixels between
the query image and the support images. However, they focus only on pixel-wise
correspondence and ignore the overall correlation of objects. In this paper, we
introduce a mask-based classification method for addressing this problem. The
mask aggregation network (MANet), which is a simple mask classification model,
is proposed to simultaneously generate a fixed number of masks and their
probabilities of being targets. Then, the final segmentation result is obtained
by aggregating all the masks according to their locations. Experiments on both
the PASCAL-5^i and COCO-20^i datasets show that our method performs comparably
to the state-of-the-art pixel-based methods. This competitive performance
demonstrates the potential of mask classification as an alternative baseline
method in few-shot semantic segmentation. Our source code will be made
available at https://github.com/TinyAway/MANet.
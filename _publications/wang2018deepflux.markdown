---
layout: publication
title: Deepflux For Skeletons In The Wild
authors: Yukang Wang, Yongchao Xu, Stavros Tsogkas, Xiang Bai, Sven Dickinson, Kaleem
  Siddiqi
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: wang2018deepflux
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.12608'}]
tags: ["CVPR"]
short_authors: Wang et al.
---
Computing object skeletons in natural images is challenging, owing to large
variations in object appearance and scale, and the complexity of handling
background clutter. Many recent methods frame object skeleton detection as a
binary pixel classification problem, which is similar in spirit to
learning-based edge detection, as well as to semantic segmentation methods. In
the present article, we depart from this strategy by training a CNN to predict
a two-dimensional vector field, which maps each scene point to a candidate
skeleton pixel, in the spirit of flux-based skeletonization algorithms. This
"image context flux" representation has two major advantages over previous
approaches. First, it explicitly encodes the relative position of skeletal
pixels to semantically meaningful entities, such as the image points in their
spatial context, and hence also the implied object boundaries. Second, since
the skeleton detection context is a region-based vector field, it is better
able to cope with object parts of large width. We evaluate the proposed method
on three benchmark datasets for skeleton detection and two for symmetry
detection, achieving consistently superior performance over state-of-the-art
methods.
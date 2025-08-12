---
layout: publication
title: 'Eigencontours: Novel Contour Descriptors Based On Low-rank Approximation'
authors: Wonhui Park, Dongkwon Jin, Chang-Su Kim
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: park2022eigencontours
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.15259'}]
tags: ["CVPR"]
short_authors: Wonhui Park, Dongkwon Jin, Chang-Su Kim
---
Novel contour descriptors, called eigencontours, based on low-rank
approximation are proposed in this paper. First, we construct a contour matrix
containing all object boundaries in a training set. Second, we decompose the
contour matrix into eigencontours via the best rank-M approximation. Third, we
represent an object boundary by a linear combination of the M eigencontours. We
also incorporate the eigencontours into an instance segmentation framework.
Experimental results demonstrate that the proposed eigencontours can represent
object boundaries more effectively and more efficiently than existing
descriptors in a low-dimensional space. Furthermore, the proposed algorithm
yields meaningful performances on instance segmentation datasets.
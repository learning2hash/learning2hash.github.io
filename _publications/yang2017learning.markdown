---
layout: publication
title: Learning Efficient Image Representation For Person Re-identification
authors: Yang Yang, Shengcai Liao, Zhen Lei, Stan Z. Li
conference: Arxiv
year: 2017
bibkey: yang2017learning
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.02319'}]
tags: []
short_authors: Yang et al.
---
Color names based image representation is successfully used in person
re-identification, due to the advantages of being compact, intuitively
understandable as well as being robust to photometric variance. However, there
exists the diversity between underlying distribution of color names' RGB values
and that of image pixels' RGB values, which may lead to inaccuracy when
directly comparing them in Euclidean space. In this paper, we propose a new
method named soft Gaussian mapping (SGM) to address this problem. We model the
discrepancies between color names and pixels using a Gaussian and utilize the
inverse of covariance matrix to bridge the gap between them. Based on SGM, an
image could be converted to several soft Gaussian maps. In each soft Gaussian
map, we further seek to establish stable and robust descriptors within a local
region through a max pooling operation. Then, a robust image representation
based on color names is obtained by concatenating the statistical descriptors
in each stripe. When labeled data are available, one discriminative subspace
projection matrix is learned to build efficient representations of an image via
cross-view coupling learning. Experiments on the public datasets - VIPeR,
PRID450S and CUHK03, demonstrate the effectiveness of our method.
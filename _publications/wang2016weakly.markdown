---
layout: publication
title: 'Weakly Supervised Patchnets: Describing And Aggregating Local Patches For
  Scene Recognition'
authors: Zhe Wang, Limin Wang, Yali Wang, Bowen Zhang, Yu Qiao
conference: IEEE Transactions on Image Processing
year: 2017
bibkey: wang2016weakly
citations: 93
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.00153'}]
tags: ["Supervised"]
short_authors: Wang et al.
---
Traditional feature encoding scheme (e.g., Fisher vector) with local
descriptors (e.g., SIFT) and recent convolutional neural networks (CNNs) are
two classes of successful methods for image recognition. In this paper, we
propose a hybrid representation, which leverages the discriminative capacity of
CNNs and the simplicity of descriptor encoding schema for image recognition,
with a focus on scene recognition. To this end, we make three main
contributions from the following aspects. First, we propose a patch-level and
end-to-end architecture to model the appearance of local patches, called \{\em
PatchNet\}. PatchNet is essentially a customized network trained in a weakly
supervised manner, which uses the image-level supervision to guide the
patch-level feature extraction. Second, we present a hybrid visual
representation, called \{\em VSAD\}, by utilizing the robust feature
representations of PatchNet to describe local patches and exploiting the
semantic probabilities of PatchNet to aggregate these local patches into a
global representation. Third, based on the proposed VSAD representation, we
propose a new state-of-the-art scene recognition approach, which achieves an
excellent performance on two standard benchmarks: MIT Indoor67 (86.2%) and
SUN397 (73.0%).
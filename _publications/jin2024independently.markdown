---
layout: publication
title: Independently Keypoint Learning For Small Object Semantic Correspondence
authors: Hailong Jin, Huiying Li
conference: Arxiv
year: 2024
bibkey: jin2024independently
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.02678'}]
tags: []
short_authors: Hailong Jin, Huiying Li
---
Semantic correspondence remains a challenging task for establishing
correspondences between a pair of images with the same category or similar
scenes due to the large intra-class appearance. In this paper, we introduce a
novel problem called 'Small Object Semantic Correspondence (SOSC).' This
problem is challenging due to the close proximity of keypoints associated with
small objects, which results in the fusion of these respective features. It is
difficult to identify the corresponding key points of the fused features, and
it is also difficult to be recognized. To address this challenge, we propose
the Keypoint Bounding box-centered Cropping (KBC) method, which aims to
increase the spatial separation between keypoints of small objects, thereby
facilitating independent learning of these keypoints. The KBC method is
seamlessly integrated into our proposed inference pipeline and can be easily
incorporated into other methodologies, resulting in significant performance
enhancements. Additionally, we introduce a novel framework, named KBCNet, which
serves as our baseline model. KBCNet comprises a Cross-Scale Feature Alignment
(CSFA) module and an efficient 4D convolutional decoder. The CSFA module is
designed to align multi-scale features, enriching keypoint representations by
integrating fine-grained features and deep semantic features. Meanwhile, the 4D
convolutional decoder, based on efficient 4D convolution, ensures efficiency
and rapid convergence. To empirically validate the effectiveness of our
proposed methodology, extensive experiments are conducted on three widely used
benchmarks: PF-PASCAL, PF-WILLOW, and SPair-71k. Our KBC method demonstrates a
substantial performance improvement of 7.5% on the SPair-71K dataset,
providing compelling evidence of its efficacy.
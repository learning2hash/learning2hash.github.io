---
layout: publication
title: 'ALIKED: A Lighter Keypoint And Descriptor Extraction Network Via Deformable
  Transformation'
authors: Xiaoming Zhao, Xingming Wu, Weihai Chen, Peter C. Y. Chen, Qingsong Xu, Zhengguo
  Li
conference: IEEE Transactions on Instrumentation and Measurement
year: 2023
bibkey: zhao2023aliked
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03608'}]
tags: ["Evaluation"]
short_authors: Zhao et al.
---
Image keypoints and descriptors play a crucial role in many visual
measurement tasks. In recent years, deep neural networks have been widely used
to improve the performance of keypoint and descriptor extraction. However, the
conventional convolution operations do not provide the geometric invariance
required for the descriptor. To address this issue, we propose the Sparse
Deformable Descriptor Head (SDDH), which learns the deformable positions of
supporting features for each keypoint and constructs deformable descriptors.
Furthermore, SDDH extracts descriptors at sparse keypoints instead of a dense
descriptor map, which enables efficient extraction of descriptors with strong
expressiveness. In addition, we relax the neural reprojection error (NRE) loss
from dense to sparse to train the extracted sparse descriptors. Experimental
results show that the proposed network is both efficient and powerful in
various visual measurement tasks, including image matching, 3D reconstruction,
and visual relocalization.
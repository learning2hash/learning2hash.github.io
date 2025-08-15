---
layout: publication
title: Efficient Texture Retrieval Using Multiscale Local Extrema Descriptors And
  Covariance Embedding
authors: Minh-tan Pham
conference: Lecture Notes in Computer Science
year: 2019
bibkey: pham2018efficient
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.01124'}]
tags: ["Evaluation"]
short_authors: Minh-tan Pham
---
This paper presents an efficient method for texture retrieval using
multiscale feature extraction and embedding based on the local extrema
keypoints. The idea is to first represent each texture image by its local
maximum and local minimum pixels. The image is then divided into regular
overlapping blocks and each one is characterized by a feature vector
constructed from the radiometric, geometric and structural information of its
local extrema. All feature vectors are finally embedded into a covariance
matrix which will be exploited for dissimilarity measurement within retrieval
task. Thanks to the method's simplicity, multiscale scheme can be easily
implemented to improve its scale-space representation capacity. We argue that
our handcrafted features are easy to implement, fast to run but can provide
very competitive performance compared to handcrafted and CNN-based learned
descriptors from the literature. In particular, the proposed framework provides
highly competitive retrieval rate for several texture databases including
94.95% for MIT Vistex, 79.87% for Stex, 76.15% for Outex TC-00013 and 89.74%
for USPtex.
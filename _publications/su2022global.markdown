---
layout: publication
title: Global Learnable Attention For Single Image Super-resolution
authors: Jian-nan Su, Min Gan, Guang-yong Chen, Jia-li Yin, C. L. Philip Chen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: su2022global
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.01057'}]
tags: []
short_authors: Su et al.
---
Self-similarity is valuable to the exploration of non-local textures in
single image super-resolution (SISR). Researchers usually assume that the
importance of non-local textures is positively related to their similarity
scores. In this paper, we surprisingly found that when repairing severely
damaged query textures, some non-local textures with low-similarity which are
closer to the target can provide more accurate and richer details than the
high-similarity ones. In these cases, low-similarity does not mean inferior but
is usually caused by different scales or orientations. Utilizing this finding,
we proposed a Global Learnable Attention (GLA) to adaptively modify similarity
scores of non-local textures during training instead of only using a fixed
similarity scoring function such as the dot product. The proposed GLA can
explore non-local textures with low-similarity but more accurate details to
repair severely damaged textures. Furthermore, we propose to adopt Super-Bit
Locality-Sensitive Hashing (SB-LSH) as a preprocessing method for our GLA. With
the SB-LSH, the computational complexity of our GLA is reduced from quadratic
to asymptotic linear with respect to the image size. In addition, the proposed
GLA can be integrated into existing deep SISR models as an efficient general
building block. Based on the GLA, we constructed a Deep Learnable Similarity
Network (DLSN), which achieves state-of-the-art performance for SISR tasks of
different degradation types (e.g. blur and noise). Our code and a pre-trained
DLSN have been uploaded to GitHub\{\dag\} for validation.
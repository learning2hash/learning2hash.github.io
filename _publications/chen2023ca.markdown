---
layout: publication
title: 'Ca-jaccard: Camera-aware Jaccard Distance For Person Re-identification'
authors: Yiyu Chen, Zheyi Fan, Zhaoru Chen, Yixuan Zhu
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: chen2023ca
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.10605'}]
tags: ["CVPR", "Distance Metric Learning", "Hybrid ANN Methods", "Re-Ranking"]
short_authors: Chen et al.
---
Person re-identification (re-ID) is a challenging task that aims to learn
discriminative features for person retrieval. In person re-ID, Jaccard distance
is a widely used distance metric, especially in re-ranking and clustering
scenarios. However, we discover that camera variation has a significant
negative impact on the reliability of Jaccard distance. In particular, Jaccard
distance calculates the distance based on the overlap of relevant neighbors.
Due to camera variation, intra-camera samples dominate the relevant neighbors,
which reduces the reliability of the neighbors by introducing intra-camera
negative samples and excluding inter-camera positive samples. To overcome this
problem, we propose a novel camera-aware Jaccard (CA-Jaccard) distance that
leverages camera information to enhance the reliability of Jaccard distance.
Specifically, we design camera-aware k-reciprocal nearest neighbors (CKRNNs) to
find k-reciprocal nearest neighbors on the intra-camera and inter-camera
ranking lists, which improves the reliability of relevant neighbors and
guarantees the contribution of inter-camera samples in the overlap. Moreover,
we propose a camera-aware local query expansion (CLQE) to mine reliable samples
in relevant neighbors by exploiting camera variation as a strong constraint and
assign these samples higher weights in overlap, further improving the
reliability. Our CA-Jaccard distance is simple yet effective and can serve as a
general distance metric for person re-ID methods with high reliability and low
computational cost. Extensive experiments demonstrate the effectiveness of our
method.
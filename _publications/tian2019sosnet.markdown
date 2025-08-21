---
layout: publication
title: 'Sosnet: Second Order Similarity Regularization For Local Descriptor Learning'
authors: Yurun Tian, Xin Yu, Bin Fan, Fuchao Wu, Huub Heijnen, Vassileios Balntas
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: tian2019sosnet
citations: 320
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.05019'}]
tags: ["CVPR", "Evaluation"]
short_authors: Tian et al.
---
Despite the fact that Second Order Similarity (SOS) has been used with
significant success in tasks such as graph matching and clustering, it has not
been exploited for learning local descriptors. In this work, we explore the
potential of SOS in the field of descriptor learning by building upon the
intuition that a positive pair of matching points should exhibit similar
distances with respect to other points in the embedding space. Thus, we propose
a novel regularization term, named Second Order Similarity Regularization
(SOSR), that follows this principle. By incorporating SOSR into training, our
learned descriptor achieves state-of-the-art performance on several challenging
benchmarks containing distinct tasks ranging from local patch retrieval to
structure from motion. Furthermore, by designing a von Mises-Fischer
distribution based evaluation method, we link the utilization of the descriptor
space to the matching performance, thus demonstrating the effectiveness of our
proposed SOSR. Extensive experimental results, empirical evidence, and in-depth
analysis are provided, indicating that SOSR can significantly boost the
matching performance of the learned descriptor.
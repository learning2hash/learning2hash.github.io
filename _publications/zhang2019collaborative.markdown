---
layout: publication
title: Collaborative Quantization For Cross-modal Similarity Search
authors: Zhang Ting, Wang Jingdong
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: zhang2019collaborative
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.00623'}]
tags: ["Hashing-Methods", "Distance-Metric-Learning", "Quantization", "CVPR", "Similarity-Search", "Datasets", "Evaluation"]
short_authors: Zhang Ting, Wang Jingdong
---
Cross-modal similarity search is a problem about designing a search system
supporting querying across content modalities, e.g., using an image to search
for texts or using a text to search for images. This paper presents a compact
coding solution for efficient search, with a focus on the quantization approach
which has already shown the superior performance over the hashing solutions in
the single-modal similarity search. We propose a cross-modal quantization
approach, which is among the early attempts to introduce quantization into
cross-modal search. The major contribution lies in jointly learning the
quantizers for both modalities through aligning the quantized representations
for each pair of image and text belonging to a document. In addition, our
approach simultaneously learns the common space for both modalities in which
quantization is conducted to enable efficient and effective search using the
Euclidean distance computed in the common space with fast distance table
lookup. Experimental results compared with several competitive algorithms over
three benchmark datasets demonstrate that the proposed approach achieves the
state-of-the-art performance.
---
layout: publication
title: 'Fast Feature Matching Of UAV Images Via Matrix Band Reduction-based GPU Data Schedule'
authors: San Jiang, Kan You, Wanshou Jiang, Qingquan Li
conference: "Arxiv"
year: 2025
citations: 0
bibkey: jiang2025fast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2505.22089'}
tags: ['Cross-Modal', 'Unsupervised', 'Efficiency', 'Retrieval Models', 'Shallow', 'Datasets', 'Vector Indexing', 'Hashing', 'Applications']
---
Feature matching dominats the time costs in structure from motion (SfM). The primary contribution of this study is a GPU data schedule algorithm for efficient feature matching of Unmanned aerial vehicle (UAV) images. The core idea is to divide the whole dataset into blocks based on the matrix band reduction (MBR) and achieve efficient feature matching via GPU-accelerated cascade hashing. First, match pairs are selected by using an image retrieval technique, which converts images into global descriptors and searches high-dimension nearest neighbors with graph indexing. Second, compact image blocks are iteratively generated from a MBR-based data schedule strategy, which exploits image connections to avoid redundant data IO (input/output) burden and increases the usage of GPU computing power. Third, guided by the generated image blocks, feature matching is executed sequentially within the framework of GPU-accelerated cascade hashing, and initial candidate matches are refined by combining a local geometric constraint and RANSAC-based global verification. For further performance improvement, these two seps are designed to execute parallelly in GPU and CPU. Finally, the performance of the proposed solution is evaluated by using large-scale UAV datasets. The results demonstrate that it increases the efficiency of feature matching with speedup ratios ranging from 77.0 to 100.0 compared with KD-Tree based matching methods, and achieves comparable accuracy in relative and absolute bundle adjustment (BA). The proposed algorithm is an efficient solution for feature matching of UAV images.

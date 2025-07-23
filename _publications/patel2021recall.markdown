---
layout: publication
title: Recall@k Surrogate Loss With Large Batches And Similarity Mixup
authors: Patel Yash, Tolias Giorgos, Matas Jiri
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: patel2021recall
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.11179'}]
tags: ["CVPR", "Distance Metric Learning", "Evaluation", "Similarity Search"]
short_authors: Patel Yash, Tolias Giorgos, Matas Jiri
---
This work focuses on learning deep visual representation models for retrieval
by exploring the interplay between a new loss function, the batch size, and a
new regularization approach. Direct optimization, by gradient descent, of an
evaluation metric, is not possible when it is non-differentiable, which is the
case for recall in retrieval. A differentiable surrogate loss for the recall is
proposed in this work. Using an implementation that sidesteps the hardware
constraints of the GPU memory, the method trains with a very large batch size,
which is essential for metrics computed on the entire retrieval database. It is
assisted by an efficient mixup regularization approach that operates on
pairwise scalar similarities and virtually increases the batch size further.
The suggested method achieves state-of-the-art performance in several image
retrieval benchmarks when used for deep metric learning. For instance-level
recognition, the method outperforms similar approaches that train using an
approximation of average precision.
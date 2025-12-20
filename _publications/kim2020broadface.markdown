---
layout: publication
title: 'Broadface: Looking At Tens Of Thousands Of People At Once For Face Recognition'
authors: Yonghyun Kim, Wonpyo Park, Jongju Shin
conference: Lecture Notes in Computer Science
year: 2020
bibkey: kim2020broadface
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.06674'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: Yonghyun Kim, Wonpyo Park, Jongju Shin
---
The datasets of face recognition contain an enormous number of identities and
instances. However, conventional methods have difficulty in reflecting the
entire distribution of the datasets because a mini-batch of small size contains
only a small portion of all identities. To overcome this difficulty, we propose
a novel method called BroadFace, which is a learning process to consider a
massive set of identities, comprehensively. In BroadFace, a linear classifier
learns optimal decision boundaries among identities from a large number of
embedding vectors accumulated over past iterations. By referring more instances
at once, the optimality of the classifier is naturally increased on the entire
datasets. Thus, the encoder is also globally optimized by referring the weight
matrix of the classifier. Moreover, we propose a novel compensation method to
increase the number of referenced instances in the training stage. BroadFace
can be easily applied on many existing methods to accelerate a learning process
and obtain a significant improvement in accuracy without extra computational
burden at inference stage. We perform extensive ablation studies and
experiments on various datasets to show the effectiveness of BroadFace, and
also empirically prove the validity of our compensation method. BroadFace
achieves the state-of-the-art results with significant improvements on nine
datasets in 1:1 face verification and 1:N face identification tasks, and is
also effective in image retrieval.
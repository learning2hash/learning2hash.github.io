---
layout: publication
title: 'Context Recovery And Knowledge Retrieval: A Novel Two-stream Framework For
  Video Anomaly Detection'
authors: Cao Congqi, Lu Yue, Zhang Yanning
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: cao2022context
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.02899'}]
tags: [DATASETS, Tools & Libraries, Hashing Methods, Evaluation]
---
Video anomaly detection aims to find the events in a video that do not
conform to the expected behavior. The prevalent methods mainly detect anomalies
by snippet reconstruction or future frame prediction error. However, the error
is highly dependent on the local context of the current snippet and lacks the
understanding of normality. To address this issue, we propose to detect
anomalous events not only by the local context, but also according to the
consistency between the testing event and the knowledge about normality from
the training data. Concretely, we propose a novel two-stream framework based on
context recovery and knowledge retrieval, where the two streams can complement
each other. For the context recovery stream, we propose a spatiotemporal U-Net
which can fully utilize the motion information to predict the future frame.
Furthermore, we propose a maximum local error mechanism to alleviate the
problem of large recovery errors caused by complex foreground objects. For the
knowledge retrieval stream, we propose an improved learnable locality-sensitive
hashing, which optimizes hash functions via a Siamese network and a mutual
difference loss. The knowledge about normality is encoded and stored in hash
tables, and the distance between the testing event and the knowledge
representation is used to reveal the probability of anomaly. Finally, we fuse
the anomaly scores from the two streams to detect anomalies. Extensive
experiments demonstrate the effectiveness and complementarity of the two
streams, whereby the proposed two-stream framework achieves state-of-the-art
performance on four datasets.
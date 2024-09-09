---
layout: publication
title: "Cross-modal Zero-shot Hashing by Label Attributes Embedding"
authors: Wang Runmin, Yu Guoxian, Liu Lei, Cui Lizhen, Domeniconi Carlotta, Zhang Xiangliang
conference: Arxiv
year: 2021
bibkey: wang2021cross
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2111.04080"}
tags: ['ARXIV', 'Cross Modal']
---
Cross-modal hashing (CMH) is one of the most promising methods in cross-modal
approximate nearest neighbor search. Most CMH solutions ideally assume the
labels of training and testing set are identical. However, the assumption is
often violated, causing a zero-shot CMH problem. Recent efforts to address this
issue focus on transferring knowledge from the seen classes to the unseen ones
using label attributes. However, the attributes are isolated from the features
of multi-modal data. To reduce the information gap, we introduce an approach
called LAEH (Label Attributes Embedding for zero-shot cross-modal Hashing). LAEH
first gets the initial semantic attribute vectors of labels by word2vec model
and then uses a transformation network to transform them into a common subspace.
Next, it leverages the hash vectors and the feature similarity matrix to guide
the feature extraction network of different modalities. At the same time, LAEH
uses the attribute similarity as the supplement of label similarity to rectify
the label embedding and common subspace. Experiments show that LAEH outperforms
related representative zero-shot and cross-modal hashing methods.

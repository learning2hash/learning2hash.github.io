---
layout: publication
title: Ranked List Loss For Deep Metric Learning
authors: Xinshao Wang, Yang Hua, Elyor Kodirov, Neil M. Robertson
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: wang2019ranked
citations: 239
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.03238'}]
tags: [Evaluation, Distance Metric Learning, CVPR, Few-shot & Zero-shot]
short_authors: Wang et al.
---
The objective of deep metric learning (DML) is to learn embeddings that can
capture semantic similarity and dissimilarity information among data points.
Existing pairwise or tripletwise loss functions used in DML are known to suffer
from slow convergence due to a large proportion of trivial pairs or triplets as
the model improves. To improve this, ranking-motivated structured losses are
proposed recently to incorporate multiple examples and exploit the structured
information among them. They converge faster and achieve state-of-the-art
performance. In this work, we unveil two limitations of existing
ranking-motivated structured losses and propose a novel ranked list loss to
solve both of them. First, given a query, only a fraction of data points is
incorporated to build the similarity structure. Consequently, some useful
examples are ignored and the structure is less informative. To address this, we
propose to build a set-based similarity structure by exploiting all instances
in the gallery. The learning setting can be interpreted as few-shot retrieval:
given a mini-batch, every example is iteratively used as a query, and the rest
ones compose the gallery to search, i.e., the support set in few-shot setting.
The rest examples are split into a positive set and a negative set. For every
mini-batch, the learning objective of ranked list loss is to make the query
closer to the positive set than to the negative set by a margin. Second,
previous methods aim to pull positive pairs as close as possible in the
embedding space. As a result, the intraclass data distribution tends to be
extremely compressed. In contrast, we propose to learn a hypersphere for each
class in order to preserve useful similarity structure inside it, which
functions as regularisation. Extensive experiments demonstrate the superiority
of our proposal by comparing with the state-of-the-art methods.
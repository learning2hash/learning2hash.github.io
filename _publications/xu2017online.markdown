---
layout: publication
title: Online Product Quantization
authors: Donna Xu, Ivor W. Tsang, Ying Zhang
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2017
bibkey: xu2017online
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.10775'}]
tags: [Evaluation, Efficiency, Similarity Search, Quantization, Scalability, Hashing
    Methods]
short_authors: Donna Xu, Ivor W. Tsang, Ying Zhang
---
Approximate nearest neighbor (ANN) search has achieved great success in many
tasks. However, existing popular methods for ANN search, such as hashing and
quantization methods, are designed for static databases only. They cannot
handle well the database with data distribution evolving dynamically, due to
the high computational effort for retraining the model based on the new
database. In this paper, we address the problem by developing an online product
quantization (online PQ) model and incrementally updating the quantization
codebook that accommodates to the incoming streaming data. Moreover, to further
alleviate the issue of large scale computation for the online PQ update, we
design two budget constraints for the model to update partial PQ codebook
instead of all. We derive a loss bound which guarantees the performance of our
online PQ model. Furthermore, we develop an online PQ model over a sliding
window with both data insertion and deletion supported, to reflect the
real-time behaviour of the data. The experiments demonstrate that our online PQ
model is both time-efficient and effective for ANN search in dynamic large
scale databases compared with baseline methods and the idea of partial PQ
codebook update further reduces the update cost.
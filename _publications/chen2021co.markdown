---
layout: publication
title: 'Co-bert: A Context-aware BERT Retrieval Model Incorporating Local And Query-specific
  Context'
authors: Xiaoyang Chen, Kai Hui, Ben He, Xianpei Han, Le Sun, Zheng Ye
conference: Arxiv
year: 2021
bibkey: chen2021co
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08523'}]
tags: [Evaluation, Re-ranking, Hybrid ANN Methods]
short_authors: Chen et al.
---
BERT-based text ranking models have dramatically advanced the
state-of-the-art in ad-hoc retrieval, wherein most models tend to consider
individual query-document pairs independently. In the mean time, the importance
and usefulness to consider the cross-documents interactions and the
query-specific characteristics in a ranking model have been repeatedly
confirmed, mostly in the context of learning to rank. The BERT-based ranking
model, however, has not been able to fully incorporate these two types of
ranking context, thereby ignoring the inter-document relationships from the
ranking and the differences among queries. To mitigate this gap, in this work,
an end-to-end transformer-based ranking model, named Co-BERT, has been proposed
to exploit several BERT architectures to calibrate the query-document
representations using pseudo relevance feedback before modeling the relevance
of a group of documents jointly. Extensive experiments on two standard test
collections confirm the effectiveness of the proposed model in improving the
performance of text re-ranking over strong fine-tuned BERT-Base baselines. We
plan to make our implementation open source to enable further comparisons.
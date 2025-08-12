---
layout: publication
title: Visually Aligned Word Embeddings For Improving Zero-shot Learning
authors: Ruizhi Qiao, Lingqiao Liu, Chunhua Shen, Anton van Den Hengel
conference: Arxiv
year: 2017
bibkey: qiao2017visually
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05427'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Qiao et al.
---
Zero-shot learning (ZSL) highly depends on a good semantic embedding to
connect the seen and unseen classes. Recently, distributed word embeddings
(DWE) pre-trained from large text corpus have become a popular choice to draw
such a connection. Compared with human defined attributes, DWEs are more
scalable and easier to obtain. However, they are designed to reflect semantic
similarity rather than visual similarity and thus using them in ZSL often leads
to inferior performance. To overcome this visual-semantic discrepancy, this
work proposes an objective function to re-align the distributed word embeddings
with visual information by learning a neural network to map it into a new
representation called visually aligned word embedding (VAWE). Thus the
neighbourhood structure of VAWEs becomes similar to that in the visual domain.
Note that in this work we do not design a ZSL method that projects the visual
features and semantic embeddings onto a shared space but just impose a
requirement on the structure of the mapped word embeddings. This strategy
allows the learned VAWE to generalize to various ZSL methods and visual
features. As evaluated via four state-of-the-art ZSL methods on four benchmark
datasets, the VAWE exhibit consistent performance improvement.
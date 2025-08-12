---
layout: publication
title: 'Embedmask: Embedding Coupling For One-stage Instance Segmentation'
authors: Hui Ying, Zhaojin Huang, Shu Liu, Tianjia Shao, Kun Zhou
conference: Arxiv
year: 2019
bibkey: ying2019embedmask
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01954'}]
tags: ["Evaluation"]
short_authors: Ying et al.
---
Current instance segmentation methods can be categorized into
segmentation-based methods that segment first then do clustering, and
proposal-based methods that detect first then predict masks for each instance
proposal using repooling. In this work, we propose a one-stage method, named
EmbedMask, that unifies both methods by taking advantages of them. Like
proposal-based methods, EmbedMask builds on top of detection models making it
strong in detection capability. Meanwhile, EmbedMask applies extra embedding
modules to generate embeddings for pixels and proposals, where pixel embeddings
are guided by proposal embeddings if they belong to the same instance. Through
this embedding coupling process, pixels are assigned to the mask of the
proposal if their embeddings are similar. The pixel-level clustering enables
EmbedMask to generate high-resolution masks without missing details from
repooling, and the existence of proposal embedding simplifies and strengthens
the clustering procedure to achieve high speed with higher performance than
segmentation-based methods. Without any bells and whistles, EmbedMask achieves
comparable performance as Mask R-CNN, which is the representative two-stage
method, and can produce more detailed masks at a higher speed. Code is
available at github.com/yinghdb/EmbedMask.
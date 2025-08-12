---
layout: publication
title: Agglomerative Token Clustering
authors: Joakim Bruslund Haurum, Sergio Escalera, Graham W. Taylor, Thomas B. Moeslund
conference: Arxiv
year: 2024
bibkey: haurum2024agglomerative
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.11923'}]
tags: []
short_authors: Haurum et al.
---
We present Agglomerative Token Clustering (ATC), a novel token merging method
that consistently outperforms previous token merging and pruning methods across
image classification, image synthesis, and object detection & segmentation
tasks. ATC merges clusters through bottom-up hierarchical clustering, without
the introduction of extra learnable parameters. We find that ATC achieves
state-of-the-art performance across all tasks, and can even perform on par with
prior state-of-the-art when applied off-the-shelf, i.e. without fine-tuning.
ATC is particularly effective when applied with low keep rates, where only a
small fraction of tokens are kept and retaining task performance is especially
difficult.
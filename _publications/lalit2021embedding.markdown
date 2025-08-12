---
layout: publication
title: Embedding-based Instance Segmentation In Microscopy
authors: Manan Lalit, Pavel Tomancak, Florian Jug
conference: Arxiv
year: 2021
bibkey: lalit2021embedding
citations: 7
additional_links: [{name: Code, url: 'https://github.com/juglab/EmbedSeg'}, {name: Paper,
    url: 'https://arxiv.org/abs/2101.10033'}]
tags: []
short_authors: Manan Lalit, Pavel Tomancak, Florian Jug
---
Automatic detection and segmentation of objects in 2D and 3D microscopy data
is important for countless biomedical applications. In the natural image
domain, spatial embedding-based instance segmentation methods are known to
yield high-quality results, but their utility for segmenting microscopy data is
currently little researched. Here we introduce EmbedSeg, an embedding-based
instance segmentation method which outperforms existing state-of-the-art
baselines on 2D as well as 3D microscopy datasets. Additionally, we show that
EmbedSeg has a GPU memory footprint small enough to train even on laptop GPUs,
making it accessible to virtually everyone. Finally, we introduce four new 3D
microscopy datasets, which we make publicly available alongside ground truth
training labels. Our open-source implementation is available at
https://github.com/juglab/EmbedSeg.
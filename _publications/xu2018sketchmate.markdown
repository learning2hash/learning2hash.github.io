---
layout: publication
title: Sketchmate Deep Hashing For Million-scale Human Sketch Retrieval
authors: Xu Peng, Huang Yongye, Yuan Tongtong, Pang Kaiyue, Song Yi-zhe, Xiang Tao, Hospedales Timothy M., Ma Zhanyu, Guo Jun
conference: "Arxiv"
year: 2018
bibkey: xu2018sketchmate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1804.01401"}
tags: ['ARXIV', 'CNN']
---
<p>We propose a deep hashing framework for sketch retrieval that, for
the first time, works on a multi-million scale human sketch dataset.
Leveraging on this large dataset, we explore a few sketch-specific
traits that were otherwise under-studied in prior literature. Instead of
following the conventional sketch recognition task, we introduce the
novel problem of sketch hashing retrieval which is not only more
challenging, but also offers a better testbed for large-scale sketch
analysis, since: (i) more fine-grained sketch feature learning is
required to accommodate the large variations in style and abstraction,
and (ii) a compact binary code needs to be learned at the same time to
enable efficient retrieval. Key to our network design is the embedding
of unique characteristics of human sketch, where (i) a two-branch
CNN-RNN architecture is adapted to explore the temporal ordering of
strokes, and (ii) a novel hashing loss is specifically designed to
accommodate both the temporal and abstract traits of sketches. By
working with a 3.8M sketch dataset, we show that state-of-the-art
hashing models specifically engineered for static images fail to perform
well on temporal sketch data. Our network on the other hand not only
offers the best retrieval performance on various code sizes, but also
yields the best generalization performance under a zero-shot setting and
when re-purposed for sketch recognition. Such superior performances
effectively demonstrate the benefit of our sketch-specific design.</p>

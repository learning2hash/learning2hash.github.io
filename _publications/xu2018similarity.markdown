---
layout: publication
title: Similarity R-C3D For Few-shot Temporal Activity Detection
authors: Huijuan Xu, Bingyi Kang, Ximeng Sun, Jiashi Feng, Kate Saenko, Trevor Darrell
conference: Arxiv
year: 2018
bibkey: xu2018similarity
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.10000'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Xu et al.
---
Many activities of interest are rare events, with only a few labeled examples
available. Therefore models for temporal activity detection which are able to
learn from a few examples are desirable. In this paper, we present a
conceptually simple and general yet novel framework for few-shot temporal
activity detection which detects the start and end time of the few-shot input
activities in an untrimmed video. Our model is end-to-end trainable and can
benefit from more few-shot examples. At test time, each proposal is assigned
the label of the few-shot activity class corresponding to the maximum
similarity score. Our Similarity R-C3D method outperforms previous work on
three large-scale benchmarks for temporal activity detection (THUMOS14,
ActivityNet1.2, and ActivityNet1.3 datasets) in the few-shot setting. Our code
will be made available.
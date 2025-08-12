---
layout: publication
title: Fine-grained Visual Classification Via Progressive Multi-granularity Training
  Of Jigsaw Patches
authors: Ruoyi Du, Dongliang Chang, Ayan Kumar Bhunia, Jiyang Xie, Zhanyu Ma, Yi-Zhe
  Song, Jun Guo
conference: Lecture Notes in Computer Science
year: 2020
bibkey: du2020fine
citations: 312
additional_links: [{name: Code, url: 'https://github.com/PRIS-CV/PMG-Progressive-Multi-Granularity-Training'},
  {name: Paper, url: 'https://arxiv.org/abs/2003.03836'}]
tags: []
short_authors: Du et al.
---
Fine-grained visual classification (FGVC) is much more challenging than
traditional classification tasks due to the inherently subtle intra-class
object variations. Recent works mainly tackle this problem by focusing on how
to locate the most discriminative parts, more complementary parts, and parts of
various granularities. However, less effort has been placed to which
granularities are the most discriminative and how to fuse information cross
multi-granularity. In this work, we propose a novel framework for fine-grained
visual classification to tackle these problems. In particular, we propose: (i)
a progressive training strategy that effectively fuses features from different
granularities, and (ii) a random jigsaw patch generator that encourages the
network to learn features at specific granularities. We obtain state-of-the-art
performances on several standard FGVC benchmark datasets, where the proposed
method consistently outperforms existing methods or delivers competitive
results. The code will be available at
https://github.com/PRIS-CV/PMG-Progressive-Multi-Granularity-Training.
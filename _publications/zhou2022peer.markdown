---
layout: publication
title: Peer Learning For Unbiased Scene Graph Generation
authors: Liguang Zhou, Junjie Hu, Yuhongze Zhou, Tin Lun Lam, Yangsheng Xu
conference: Arxiv
year: 2023
bibkey: zhou2022peer
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.00146'}]
tags: []
short_authors: Zhou et al.
---
Unbiased scene graph generation (USGG) is a challenging task that requires
predicting diverse and heavily imbalanced predicates between objects in an
image. To address this, we propose a novel framework peer learning that uses
predicate sampling and consensus voting (PSCV) to encourage multiple peers to
learn from each other. Predicate sampling divides the predicate classes into
sub-distributions based on frequency, and assigns different peers to handle
each sub-distribution or combinations of them. Consensus voting ensembles the
peers' complementary predicate knowledge by emphasizing majority opinion and
diminishing minority opinion. Experiments on Visual Genome show that PSCV
outperforms previous methods and achieves a new state-of-the-art on SGCls task
with 31.6 mean.
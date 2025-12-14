---
layout: publication
title: Domain Adaptation In Multi-view Embedding For Cross-modal Video Retrieval
authors: Jonathan Munro, Michael Wray, Diane Larlus, Gabriela Csurka, Dima Damen
conference: Arxiv
year: 2021
bibkey: munro2021domain
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.12812'}]
tags: [Video Retrieval, Evaluation, Supervised, Unsupervised]
short_authors: Munro et al.
---
Given a gallery of uncaptioned video sequences, this paper considers the task
of retrieving videos based on their relevance to an unseen text query. To
compensate for the lack of annotations, we rely instead on a related video
gallery composed of video-caption pairs, termed the source gallery, albeit with
a domain gap between its videos and those in the target gallery. We thus
introduce the problem of Unsupervised Domain Adaptation for Cross-modal Video
Retrieval, along with a new benchmark on fine-grained actions. We propose a
novel iterative domain alignment method by means of pseudo-labelling target
videos and cross-domain (i.e. source-target) ranking. Our approach adapts the
embedding space to the target gallery, consistently outperforming source-only
as well as marginal and conditional alignment methods.
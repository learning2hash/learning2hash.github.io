---
layout: publication
title: Core Tokensets For Data-efficient Sequential Training Of Transformers
authors: Subarnaduti Paul, Manuel Brack, Patrick Schramowski, Kristian Kersting, Martin
  Mundt
conference: Arxiv
year: 2024
bibkey: paul2024core
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.05800'}]
tags: []
short_authors: Paul et al.
---
Deep networks are frequently tuned to novel tasks and continue learning from
ongoing data streams. Such sequential training requires consolidation of new
and past information, a challenge predominantly addressed by retaining the most
important data points - formally known as coresets. Traditionally, these
coresets consist of entire samples, such as images or sentences. However,
recent transformer architectures operate on tokens, leading to the famous
assertion that an image is worth 16x16 words. Intuitively, not all of these
tokens are equally informative or memorable. Going beyond coresets, we thus
propose to construct a deeper-level data summary on the level of tokens. Our
respectively named core tokensets both select the most informative data points
and leverage feature attribution to store only their most relevant features. We
demonstrate that core tokensets yield significant performance retention in
incremental image classification, open-ended visual question answering, and
continual image captioning with significantly reduced memory. In fact, we
empirically find that a core tokenset of 1% of the data performs comparably to
at least a twice as large and up to 10 times larger coreset.
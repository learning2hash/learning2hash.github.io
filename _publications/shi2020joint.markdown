---
layout: publication
title: Joint Embedding In Named Entity Linking On Sentence Level
authors: Wei Shi, Siyuan Zhang, Zhiwei Zhang, Hong Cheng, Jeffrey Xu Yu
conference: Arxiv
year: 2020
bibkey: shi2020joint
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.04936'}]
tags: []
short_authors: Shi et al.
---
Named entity linking is to map an ambiguous mention in documents to an entity
in a knowledge base. The named entity linking is challenging, given the fact
that there are multiple candidate entities for a mention in a document. It is
difficult to link a mention when it appears multiple times in a document, since
there are conflicts by the contexts around the appearances of the mention. In
addition, it is difficult since the given training dataset is small due to the
reason that it is done manually to link a mention to its mapping entity. In the
literature, there are many reported studies among which the recent embedding
methods learn vectors of entities from the training dataset at document level.
To address these issues, we focus on how to link entity for mentions at a
sentence level, which reduces the noises introduced by different appearances of
the same mention in a document at the expense of insufficient information to be
used. We propose a new unified embedding method by maximizing the relationships
learned from knowledge graphs. We confirm the effectiveness of our method in
our experimental studies.
---
layout: publication
title: 'FMA: A Dataset For Music Analysis'
authors: "Micha\xEBl Defferrard, Kirell Benzi, Pierre Vandergheynst, Xavier Bresson"
conference: Arxiv
year: 2016
bibkey: defferrard2016fma
citations: 165
additional_links: [{name: Code, url: 'https://github.com/mdeff/fma'}, {name: Paper,
    url: 'https://arxiv.org/abs/1612.01840'}]
tags: ["Datasets"]
short_authors: Defferrard et al.
---
We introduce the Free Music Archive (FMA), an open and easily accessible
dataset suitable for evaluating several tasks in MIR, a field concerned with
browsing, searching, and organizing large music collections. The community's
growing interest in feature and end-to-end learning is however restrained by
the limited availability of large audio datasets. The FMA aims to overcome this
hurdle by providing 917 GiB and 343 days of Creative Commons-licensed audio
from 106,574 tracks from 16,341 artists and 14,854 albums, arranged in a
hierarchical taxonomy of 161 genres. It provides full-length and high-quality
audio, pre-computed features, together with track- and user-level metadata,
tags, and free-form text such as biographies. We here describe the dataset and
how it was created, propose a train/validation/test split and three subsets,
discuss some suitable MIR tasks, and evaluate some baselines for genre
recognition. Code, data, and usage examples are available at
https://github.com/mdeff/fma
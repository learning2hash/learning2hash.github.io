---
layout: publication
title: 'Snap And Find: Deep Discrete Cross-domain Garment Image Retrieval'
authors: Yadan Luo, Ziwei Wang, Zi Huang, Yang Yang, Huimin Lu
conference: Arxiv
year: 2019
bibkey: luo2019snap
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.02887'}]
tags: ["Image Retrieval"]
short_authors: Luo et al.
---
With the increasing number of online stores, there is a pressing need for
intelligent search systems to understand the item photos snapped by customers
and search against large-scale product databases to find their desired items.
However, it is challenging for conventional retrieval systems to match up the
item photos captured by customers and the ones officially released by stores,
especially for garment images. To bridge the customer- and store- provided
garment photos, existing studies have been widely exploiting the clothing
attributes (\textit\{e.g.,\} black) and landmarks (\textit\{e.g.,\} collar) to
learn a common embedding space for garment representations. Unfortunately they
omit the sequential correlation of attributes and consume large quantity of
human labors to label the landmarks. In this paper, we propose a deep
multi-task cross-domain hashing termed \textit\{DMCH\}, in which cross-domain
embedding and sequential attribute learning are modeled simultaneously.
Sequential attribute learning not only provides the semantic guidance for
embedding, but also generates rich attention on discriminative local details
(\textit\{e.g.,\} black buttons) of clothing items without requiring extra
landmark labels. This leads to promising performance and 306\\(\times\\) boost on
efficiency when compared with the state-of-the-art models, which is
demonstrated through rigorous experiments on two public fashion datasets.
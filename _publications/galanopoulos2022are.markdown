---
layout: publication
title: Are All Combinations Equal? Combining Textual And Visual Features With Multiple
  Space Learning For Text-based Video Retrieval
authors: Damianos Galanopoulos, Vasileios Mezaris
conference: Arxiv
year: 2022
bibkey: galanopoulos2022are
citations: 0
additional_links: [{name: Code, url: 'https://github.com/bmezaris/TextToVideoRetrieval-TtimesV'},
  {name: Paper, url: 'https://arxiv.org/abs/2211.11351'}]
tags: [Video Retrieval, Evaluation, Scalability, Datasets]
short_authors: Damianos Galanopoulos, Vasileios Mezaris
---
In this paper we tackle the cross-modal video retrieval problem and, more
specifically, we focus on text-to-video retrieval. We investigate how to
optimally combine multiple diverse textual and visual features into feature
pairs that lead to generating multiple joint feature spaces, which encode
text-video pairs into comparable representations. To learn these
representations our proposed network architecture is trained by following a
multiple space learning procedure. Moreover, at the retrieval stage, we
introduce additional softmax operations for revising the inferred query-video
similarities. Extensive experiments in several setups based on three
large-scale datasets (IACC.3, V3C1, and MSR-VTT) lead to conclusions on how to
best combine text-visual features and document the performance of the proposed
network. Source code is made publicly available at:
https://github.com/bmezaris/TextToVideoRetrieval-TtimesV
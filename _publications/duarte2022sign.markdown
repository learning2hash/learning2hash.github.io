---
layout: publication
title: Sign Language Video Retrieval With Free-form Textual Queries
authors: "Amanda Duarte, Samuel Albanie, Xavier Gir\xF3-I-Nieto, G\xFCl Varol"
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: duarte2022sign
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.02495'}]
tags: [Video Retrieval, Evaluation, Datasets, Scalability, CVPR, Tools & Libraries]
short_authors: Duarte et al.
---
Systems that can efficiently search collections of sign language videos have
been highlighted as a useful application of sign language technology. However,
the problem of searching videos beyond individual keywords has received limited
attention in the literature. To address this gap, in this work we introduce the
task of sign language retrieval with free-form textual queries: given a written
query (e.g., a sentence) and a large collection of sign language videos, the
objective is to find the signing video in the collection that best matches the
written query. We propose to tackle this task by learning cross-modal
embeddings on the recently introduced large-scale How2Sign dataset of American
Sign Language (ASL). We identify that a key bottleneck in the performance of
the system is the quality of the sign video embedding which suffers from a
scarcity of labeled training data. We, therefore, propose SPOT-ALIGN, a
framework for interleaving iterative rounds of sign spotting and feature
alignment to expand the scope and scale of available training data. We validate
the effectiveness of SPOT-ALIGN for learning a robust sign video embedding
through improvements in both sign recognition and the proposed video retrieval
task.
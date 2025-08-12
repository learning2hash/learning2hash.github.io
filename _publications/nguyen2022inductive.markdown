---
layout: publication
title: Inductive And Transductive Few-shot Video Classification Via Appearance And
  Temporal Alignments
authors: Khoi D. Nguyen, Quoc-Huy Tran, Khoi Nguyen, Binh-Son Hua, Rang Nguyen
conference: Lecture Notes in Computer Science
year: 2022
bibkey: nguyen2022inductive
citations: 22
additional_links: [{name: Code, url: 'https://github.com/VinAIResearch/fsvc-ata'},
  {name: Paper, url: 'https://arxiv.org/abs/2207.10785'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Nguyen et al.
---
We present a novel method for few-shot video classification, which performs
appearance and temporal alignments. In particular, given a pair of query and
support videos, we conduct appearance alignment via frame-level feature
matching to achieve the appearance similarity score between the videos, while
utilizing temporal order-preserving priors for obtaining the temporal
similarity score between the videos. Moreover, we introduce a few-shot video
classification framework that leverages the above appearance and temporal
similarity scores across multiple steps, namely prototype-based training and
testing as well as inductive and transductive prototype refinement. To the best
of our knowledge, our work is the first to explore transductive few-shot video
classification. Extensive experiments on both Kinetics and Something-Something
V2 datasets show that both appearance and temporal alignments are crucial for
datasets with temporal order sensitivity such as Something-Something V2. Our
approach achieves similar or better results than previous methods on both
datasets. Our code is available at https://github.com/VinAIResearch/fsvc-ata.
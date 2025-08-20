---
layout: publication
title: Semantic-aware Binary Code Representation With BERT
authors: Hyungjoon Koo, Soyeon Park, Daejin Choi, Taesoo Kim
conference: Arxiv
year: 2021
bibkey: koo2021semantic
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.05478'}]
tags: [Evaluation, Compact Codes]
short_authors: Koo et al.
---
A wide range of binary analysis applications, such as bug discovery, malware
analysis and code clone detection, require recovery of contextual meanings on a
binary code. Recently, binary analysis techniques based on machine learning
have been proposed to automatically reconstruct the code representation of a
binary instead of manually crafting specifics of the analysis algorithm.
However, the existing approaches utilizing machine learning are still
specialized to solve one domain of problems, rendering recreation of models for
different types of binary analysis. In this paper, we propose DeepSemantic
utilizing BERT in producing the semantic-aware code representation of a binary
code.
  To this end, we introduce well-balanced instruction normalization that holds
rich information for each of instructions yet minimizing an out-of-vocabulary
(OOV) problem. DeepSemantic has been carefully designed based on our study with
large swaths of binaries. Besides, DeepSemantic leverages the essence of the
BERT architecture into re-purposing a pre-trained generic model that is readily
available as a one-time processing, followed by quickly applying specific
downstream tasks with a fine-tuning process. We demonstrate DeepSemantic with
two downstream tasks, namely, binary similarity comparison and compiler
provenance (i.e., compiler and optimization level) prediction. Our experimental
results show that the binary similarity model outperforms two state-of-the-art
binary similarity tools, DeepBinDiff and SAFE, 49.84% and 15.83% on average,
respectively.
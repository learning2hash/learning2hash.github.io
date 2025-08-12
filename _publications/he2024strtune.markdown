---
layout: publication
title: 'Strtune: Data Dependence-based Code Slicing For Binary Similarity Detection
  With Fine-tuned Representation'
authors: Kaiyan He, Yikun Hu, Xuehui Li, Yunhao Song, Yubo Zhao, Dawu Gu
conference: IEEE Transactions on Information Forensics and Security
year: 2024
bibkey: he2024strtune
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.12454'}]
tags: []
short_authors: He et al.
---
Binary Code Similarity Detection (BCSD) is significant for software security
as it can address binary tasks such as malicious code snippets identification
and binary patch analysis by comparing code patterns. Recently, there has been
a growing focus on artificial intelligence-based approaches in BCSD due to
their scalability and generalization. Because binaries are compiled with
different compilation configurations, existing approaches still face notable
limitations when comparing binary similarity. First, BCSD requires analysis on
code behavior, and existing work claims to extract semantic, but actually still
makes analysis in terms of syntax. Second, directly extracting features from
assembly sequences, existing work cannot address the issues of instruction
reordering and different syntax expressions caused by various compilation
configurations. In this paper, we propose StrTune, which slices binary code
based on data dependence and perform slice-level fine-tuning. To address the
first limitation, StrTune performs backward slicing based on data dependence to
capture how a value is computed along the execution. Each slice reflects the
collecting semantics of the code, which is stable across different compilation
configurations. StrTune introduces flow types to emphasize the independence of
computations between slices, forming a graph representation. To overcome the
second limitation, based on slices corresponding to the same value computation
but having different syntax representation, StrTune utilizes a Siamese Network
to fine-tune such pairs, making their representations closer in the feature
space.
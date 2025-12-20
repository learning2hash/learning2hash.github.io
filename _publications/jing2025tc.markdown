---
layout: publication
title: 'TC-MGC: Text-conditioned Multi-grained Contrastive Learning For Text-video
  Retrieval'
authors: Xiaolun Jing, Genke Yang, Jian Chu
conference: Information Fusion
year: 2025
bibkey: jing2025tc
citations: 0
additional_links: [{name: Code, url: 'https://github.com/JingXiaolun/TC-MGC'}, {name: Paper,
    url: 'https://arxiv.org/abs/2504.04707'}]
tags: ["Evaluation", "Self-Supervised", "Tools & Libraries", "Video Retrieval"]
short_authors: Xiaolun Jing, Genke Yang, Jian Chu
---
Motivated by the success of coarse-grained or fine-grained contrast in
text-video retrieval, there emerge multi-grained contrastive learning methods
which focus on the integration of contrasts with different granularity.
However, due to the wider semantic range of videos, the text-agnostic video
representations might encode misleading information not described in texts,
thus impeding the model from capturing precise cross-modal semantic
correspondence. To this end, we propose a Text-Conditioned Multi-Grained
Contrast framework, dubbed TC-MGC. Specifically, our model employs a
language-video attention block to generate aggregated frame and video
representations conditioned on the word's and text's attention weights over
frames. To filter unnecessary similarity interactions and decrease trainable
parameters in the Interactive Similarity Aggregation (ISA) module, we design a
Similarity Reorganization (SR) module to identify attentive similarities and
reorganize cross-modal similarity vectors and matrices. Next, we argue that the
imbalance problem among multigrained similarities may result in over- and
under-representation issues. We thereby introduce an auxiliary Similarity
Decorrelation Regularization (SDR) loss to facilitate cooperative relationship
utilization by similarity variance minimization on matching text-video pairs.
Finally, we present a Linear Softmax Aggregation (LSA) module to explicitly
encourage the interactions between multiple similarities and promote the usage
of multi-grained information. Empirically, TC-MGC achieves competitive results
on multiple text-video retrieval benchmarks, outperforming X-CLIP model by
+2.8% (+1.3%), +2.2% (+1.0%), +1.5% (+0.9%) relative (absolute) improvements in
text-to-video retrieval R@1 on MSR-VTT, DiDeMo and VATEX, respectively. Our
code is publicly available at https://github.com/JingXiaolun/TC-MGC.
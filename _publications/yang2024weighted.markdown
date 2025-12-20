---
layout: publication
title: Weighted Kl-divergence For Document Ranking Model Refinement
authors: Yingrui Yang, Yifan Qiao, Shanxiu He, Tao Yang
conference: Proceedings of the 47th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2024
bibkey: yang2024weighted
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.05977'}]
tags: ["Datasets", "Hybrid ANN Methods", "Re-Ranking", "SIGIR", "Self-Supervised"]
short_authors: Yang et al.
---
Transformer-based retrieval and reranking models for text document search are
often refined through knowledge distillation together with contrastive
learning. A tight distribution matching between the teacher and student models
can be hard as over-calibration may degrade training effectiveness when a
teacher does not perform well. This paper contrastively reweights KL divergence
terms to prioritize the alignment between a student and a teacher model for
proper separation of positive and negative documents. This paper analyzes and
evaluates the proposed loss function on the MS MARCO and BEIR datasets to
demonstrate its effectiveness in improving the relevance of tested student
models.
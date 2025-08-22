---
layout: publication
title: Zero-shot Dense Retrieval With Momentum Adversarial Domain Invariant Representations
authors: Ji Xin, Chenyan Xiong, Ashwin Srinivasan, Ankita Sharma, Damien Jose, Paul
  N. Bennett
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: xin2021zero
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.07581'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Robustness", "Text Retrieval"]
short_authors: Xin et al.
---
Dense retrieval (DR) methods conduct text retrieval by first encoding texts
in the embedding space and then matching them by nearest neighbor search. This
requires strong locality properties from the representation space, i.e, the
close allocations of each small group of relevant texts, which are hard to
generalize to domains without sufficient training data. In this paper, we aim
to improve the generalization ability of DR models from source training domains
with rich supervision signals to target domains without any relevant labels, in
the zero-shot setting. To achieve that, we propose Momentum adversarial Domain
Invariant Representation learning (MoDIR), which introduces a momentum method
in the DR training process to train a domain classifier distinguishing source
versus target, and then adversarially updates the DR encoder to learn domain
invariant representations. Our experiments show that MoDIR robustly outperforms
its baselines on 10+ ranking datasets from the BEIR benchmark in the zero-shot
setup, with more than 10% relative gains on datasets with enough sensitivity
for DR models' evaluation. Source code of this paper will be released.
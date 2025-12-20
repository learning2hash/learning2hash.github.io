---
layout: publication
title: Poisoning Retrieval Corpora By Injecting Adversarial Passages
authors: Zexuan Zhong, Ziqing Huang, Alexander Wettig, Danqi Chen
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: zhong2023poisoning
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.19156'}]
tags: ["EMNLP", "Evaluation", "Robustness", "Supervised", "Unsupervised"]
short_authors: Zhong et al.
---
Dense retrievers have achieved state-of-the-art performance in various
information retrieval tasks, but to what extent can they be safely deployed in
real-world applications? In this work, we propose a novel attack for dense
retrieval systems in which a malicious user generates a small number of
adversarial passages by perturbing discrete tokens to maximize similarity with
a provided set of training queries. When these adversarial passages are
inserted into a large retrieval corpus, we show that this attack is highly
effective in fooling these systems to retrieve them for queries that were not
seen by the attacker. More surprisingly, these adversarial passages can
directly generalize to out-of-domain queries and corpora with a high success
attack rate -- for instance, we find that 50 generated passages optimized on
Natural Questions can mislead >94% of questions posed in financial documents or
online forums. We also benchmark and compare a range of state-of-the-art dense
retrievers, both unsupervised and supervised. Although different systems
exhibit varying levels of vulnerability, we show they can all be successfully
attacked by injecting up to 500 passages, a small fraction compared to a
retrieval corpus of millions of passages.
---
layout: publication
title: 'Deep Learning Based Dense Retrieval: A Comparative Study'
authors: Ming Zhong, Zhizhi Wu, Nanako Honda
conference: Arxiv
year: 2024
bibkey: zhong2024deep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.20315'}]
tags: [Evaluation, Supervised, Neural Hashing, Survey Paper, Robustness, Unsupervised]
short_authors: Ming Zhong, Zhizhi Wu, Nanako Honda
---
Dense retrievers have achieved state-of-the-art performance in various
information retrieval tasks, but their robustness against tokenizer poisoning
remains underexplored. In this work, we assess the vulnerability of dense
retrieval systems to poisoned tokenizers by evaluating models such as BERT,
Dense Passage Retrieval (DPR), Contriever, SimCSE, and ANCE. We find that
supervised models like BERT and DPR experience significant performance
degradation when tokenizers are compromised, while unsupervised models like
ANCE show greater resilience. Our experiments reveal that even small
perturbations can severely impact retrieval accuracy, highlighting the need for
robust defenses in critical applications.
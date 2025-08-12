---
layout: publication
title: Task Affinity With Maximum Bipartite Matching In Few-shot Learning
authors: Cat P. Le, Juncheng Dong, Mohammadreza Soltani, Vahid Tarokh
conference: Arxiv
year: 2021
bibkey: le2021task
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.02399'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Le et al.
---
We propose an asymmetric affinity score for representing the complexity of
utilizing the knowledge of one task for learning another one. Our method is
based on the maximum bipartite matching algorithm and utilizes the Fisher
Information matrix. We provide theoretical analyses demonstrating that the
proposed score is mathematically well-defined, and subsequently use the
affinity score to propose a novel algorithm for the few-shot learning problem.
In particular, using this score, we find relevant training data labels to the
test data and leverage the discovered relevant data for episodically
fine-tuning a few-shot model. Results on various few-shot benchmark datasets
demonstrate the efficacy of the proposed approach by improving the
classification accuracy over the state-of-the-art methods even when using
smaller models.
---
layout: publication
title: Mining Entity Synonyms With Efficient Neural Set Generation
authors: Jiaming Shen, Ruiliang Lyu, Xiang Ren, Michelle Vanni, Brian Sadler, Jiawei
  Han
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2019
bibkey: shen2019mining
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.07032'}]
tags: ["AAAI", "Efficiency"]
short_authors: Shen et al.
---
Mining entity synonym sets (i.e., sets of terms referring to the same entity)
is an important task for many entity-leveraging applications. Previous work
either rank terms based on their similarity to a given query term, or treats
the problem as a two-phase task (i.e., detecting synonymy pairs, followed by
organizing these pairs into synonym sets). However, these approaches fail to
model the holistic semantics of a set and suffer from the error propagation
issue. Here we propose a new framework, named SynSetMine, that efficiently
generates entity synonym sets from a given vocabulary, using example sets from
external knowledge bases as distant supervision. SynSetMine consists of two
novel modules: (1) a set-instance classifier that jointly learns how to
represent a permutation invariant synonym set and whether to include a new
instance (i.e., a term) into the set, and (2) a set generation algorithm that
enumerates the vocabulary only once and applies the learned set-instance
classifier to detect all entity synonym sets in it. Experiments on three real
datasets from different domains demonstrate both effectiveness and efficiency
of SynSetMine for mining entity synonym sets.
---
layout: publication
title: Improving Entity Disambiguation By Reasoning Over A Knowledge Base
authors: Tom Ayoola, Joseph Fisher, Andrea Pierleoni
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2022
bibkey: ayoola2022improving
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.04106'}]
tags: ["NAACL"]
short_authors: Tom Ayoola, Joseph Fisher, Andrea Pierleoni
---
Recent work in entity disambiguation (ED) has typically neglected structured
knowledge base (KB) facts, and instead relied on a limited subset of KB
information, such as entity descriptions or types. This limits the range of
contexts in which entities can be disambiguated. To allow the use of all KB
facts, as well as descriptions and types, we introduce an ED model which links
entities by reasoning over a symbolic knowledge base in a fully differentiable
fashion. Our model surpasses state-of-the-art baselines on six well-established
ED datasets by 1.3 F1 on average. By allowing access to all KB information, our
model is less reliant on popularity-based entity priors, and improves
performance on the challenging ShadowLink dataset (which emphasises infrequent
and ambiguous entities) by 12.7 F1.
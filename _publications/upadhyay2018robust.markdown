---
layout: publication
title: Robust Cross-lingual Hypernymy Detection Using Dependency Context
authors: Shyam Upadhyay, Yogarshi Vyas, Marine Carpuat, Dan Roth
conference: 'Proceedings of the 2018 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies, Volume 1
  (Long Papers)'
year: 2018
bibkey: upadhyay2018robust
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.11291'}]
tags: ["NAACL"]
short_authors: Upadhyay et al.
---
Cross-lingual Hypernymy Detection involves determining if a word in one
language ("fruit") is a hypernym of a word in another language ("pomme" i.e.
apple in French). The ability to detect hypernymy cross-lingually can aid in
solving cross-lingual versions of tasks such as textual entailment and event
coreference. We propose BISPARSE-DEP, a family of unsupervised approaches for
cross-lingual hypernymy detection, which learns sparse, bilingual word
embeddings based on dependency contexts. We show that BISPARSE-DEP can
significantly improve performance on this task, compared to approaches based
only on lexical context. Our approach is also robust, showing promise for
low-resource settings: our dependency-based embeddings can be learned using a
parser trained on related languages, with negligible loss in performance. We
also crowd-source a challenging dataset for this task on four languages --
Russian, French, Arabic, and Chinese. Our embeddings and datasets are publicly
available.
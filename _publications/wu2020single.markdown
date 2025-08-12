---
layout: publication
title: Single-/multi-source Cross-lingual NER Via Teacher-student Learning On Unlabeled
  Data In Target Language
authors: "Qianhui Wu, Zijia Lin, B\xF6rje F. Karlsson, Jian-Guang Lou, Biqing Huang"
conference: Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics
year: 2020
bibkey: wu2020single
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.12440'}]
tags: []
short_authors: Wu et al.
---
To better tackle the named entity recognition (NER) problem on languages with
little/no labeled data, cross-lingual NER must effectively leverage knowledge
learned from source languages with rich labeled data. Previous works on
cross-lingual NER are mostly based on label projection with pairwise texts or
direct model transfer. However, such methods either are not applicable if the
labeled data in the source languages is unavailable, or do not leverage
information contained in unlabeled data in the target language. In this paper,
we propose a teacher-student learning method to address such limitations, where
NER models in the source languages are used as teachers to train a student
model on unlabeled data in the target language. The proposed method works for
both single-source and multi-source cross-lingual NER. For the latter, we
further propose a similarity measuring method to better weight the supervision
from different teacher models. Extensive experiments for 3 target languages on
benchmark datasets well demonstrate that our method outperforms existing
state-of-the-art methods for both single-source and multi-source cross-lingual
NER.
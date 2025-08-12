---
layout: publication
title: Incorporating Visual Semantics Into Sentence Representations Within A Grounded
  Space
authors: Patrick Bordes, Eloi Zablocki, Laure Soulier, Benjamin Piwowarski, Patrick
  Gallinari
conference: Proceedings of the 2019 Conference on Empirical Methods in Natural Language
  Processing and the 9th International Joint Conference on Natural Language Processing
  (EMNLP-IJCNLP)
year: 2019
bibkey: bordes2019incorporating
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.02734'}]
tags: ["EMNLP"]
short_authors: Bordes et al.
---
Language grounding is an active field aiming at enriching textual
representations with visual information. Generally, textual and visual elements
are embedded in the same representation space, which implicitly assumes a
one-to-one correspondence between modalities. This hypothesis does not hold
when representing words, and becomes problematic when used to learn sentence
representations --- the focus of this paper --- as a visual scene can be
described by a wide variety of sentences. To overcome this limitation, we
propose to transfer visual information to textual representations by learning
an intermediate representation space: the grounded space. We further propose
two new complementary objectives ensuring that (1) sentences associated with
the same visual content are close in the grounded space and (2) similarities
between related elements are preserved across modalities. We show that this
model outperforms the previous state-of-the-art on classification and semantic
relatedness tasks.
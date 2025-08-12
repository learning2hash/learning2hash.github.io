---
layout: publication
title: Conditional Image-text Embedding Networks
authors: Bryan A. Plummer, Paige Kordas, M. Hadi Kiapour, Shuai Zheng, Robinson Piramuthu,
  Svetlana Lazebnik
conference: Lecture Notes in Computer Science
year: 2018
bibkey: plummer2017conditional
citations: 134
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.08389'}]
tags: []
short_authors: Plummer et al.
---
This paper presents an approach for grounding phrases in images which jointly
learns multiple text-conditioned embeddings in a single end-to-end model. In
order to differentiate text phrases into semantically distinct subspaces, we
propose a concept weight branch that automatically assigns phrases to
embeddings, whereas prior works predefine such assignments. Our proposed
solution simplifies the representation requirements for individual embeddings
and allows the underrepresented concepts to take advantage of the shared
representations before feeding them into concept-specific layers. Comprehensive
experiments verify the effectiveness of our approach across three phrase
grounding datasets, Flickr30K Entities, ReferIt Game, and Visual Genome, where
we obtain a (resp.) 4%, 3%, and 4% improvement in grounding performance over a
strong region-phrase embedding baseline.
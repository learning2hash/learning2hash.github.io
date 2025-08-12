---
layout: publication
title: Joint Learning Of The Embedding Of Words And Entities For Named Entity Disambiguation
authors: Ikuya Yamada, Hiroyuki Shindo, Hideaki Takeda, Yoshiyasu Takefuji
conference: Proceedings of The 20th SIGNLL Conference on Computational Natural Language
  Learning
year: 2016
bibkey: yamada2016joint
citations: 331
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.01343'}]
tags: []
short_authors: Yamada et al.
---
Named Entity Disambiguation (NED) refers to the task of resolving multiple
named entity mentions in a document to their correct references in a knowledge
base (KB) (e.g., Wikipedia). In this paper, we propose a novel embedding method
specifically designed for NED. The proposed method jointly maps words and
entities into the same continuous vector space. We extend the skip-gram model
by using two models. The KB graph model learns the relatedness of entities
using the link structure of the KB, whereas the anchor context model aims to
align vectors such that similar words and entities occur close to one another
in the vector space by leveraging KB anchors and their context words. By
combining contexts based on the proposed embedding with standard NED features,
we achieved state-of-the-art accuracy of 93.1% on the standard CoNLL dataset
and 85.2% on the TAC 2010 dataset.
---
layout: publication
title: Multilingual Music Genre Embeddings For Effective Cross-lingual Music Item
  Annotation
authors: Elena V. Epure, Guillaume Salha, Romain Hennequin
conference: Arxiv
year: 2020
bibkey: epure2020multilingual
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.07755'}]
tags: ["Recommender Systems"]
short_authors: Elena V. Epure, Guillaume Salha, Romain Hennequin
---
Annotating music items with music genres is crucial for music recommendation
and information retrieval, yet challenging given that music genres are
subjective concepts. Recently, in order to explicitly consider this
subjectivity, the annotation of music items was modeled as a translation task:
predict for a music item its music genres within a target vocabulary or
taxonomy (tag system) from a set of music genre tags originating from other tag
systems. However, without a parallel corpus, previous solutions could not
handle tag systems in other languages, being limited to the English-language
only. Here, by learning multilingual music genre embeddings, we enable
cross-lingual music genre translation without relying on a parallel corpus.
First, we apply compositionality functions on pre-trained word embeddings to
represent multi-word tags.Second, we adapt the tag representations to the music
domain by leveraging multilingual music genres graphs with a modified
retrofitting algorithm. Experiments show that our method: 1) is effective in
translating music genres across tag systems in multiple languages (English,
French and Spanish); 2) outperforms the previous baseline in an
English-language multi-source translation task. We publicly release the new
multilingual data and code.
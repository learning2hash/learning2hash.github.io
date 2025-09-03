---
layout: publication
title: 'Wikimatrix: Mining 135M Parallel Sentences In 1620 Language Pairs From Wikipedia'
authors: "Holger Schwenk, Vishrav Chaudhary, Shuo Sun, Hongyu Gong, Francisco Guzm\xE1\
  n"
conference: Arxiv
year: 2019
bibkey: schwenk2019wikimatrix
citations: 152
additional_links: [{name: Other, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/1907.05791'}]
tags: ["Uncategorized"]
short_authors: Schwenk et al.
---
We present an approach based on multilingual sentence embeddings to
automatically extract parallel sentences from the content of Wikipedia articles
in 85 languages, including several dialects or low-resource languages. We do
not limit the the extraction process to alignments with English, but
systematically consider all possible language pairs. In total, we are able to
extract 135M parallel sentences for 1620 different language pairs, out of which
only 34M are aligned with English. This corpus of parallel sentences is freely
available at
https://github.com/facebookresearch/LASER/tree/master/tasks/WikiMatrix. To get
an indication on the quality of the extracted bitexts, we train neural MT
baseline systems on the mined data only for 1886 languages pairs, and evaluate
them on the TED corpus, achieving strong BLEU scores for many language pairs.
The WikiMatrix bitexts seem to be particularly interesting to train MT systems
between distant languages without the need to pivot through English.
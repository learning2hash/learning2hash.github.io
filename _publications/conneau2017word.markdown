---
layout: publication
title: Word Translation Without Parallel Data
authors: "Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer,\
  \ Herv\xE9 J\xE9gou"
conference: Arxiv
year: 2017
bibkey: conneau2017word
citations: 760
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.04087'}]
tags: ["Unsupervised"]
short_authors: Conneau et al.
---
State-of-the-art methods for learning cross-lingual word embeddings have
relied on bilingual dictionaries or parallel corpora. Recent studies showed
that the need for parallel data supervision can be alleviated with
character-level information. While these methods showed encouraging results,
they are not on par with their supervised counterparts and are limited to pairs
of languages sharing a common alphabet. In this work, we show that we can build
a bilingual dictionary between two languages without using any parallel
corpora, by aligning monolingual word embedding spaces in an unsupervised way.
Without using any character information, our model even outperforms existing
supervised methods on cross-lingual tasks for some language pairs. Our
experiments demonstrate that our method works very well also for distant
language pairs, like English-Russian or English-Chinese. We finally describe
experiments on the English-Esperanto low-resource language pair, on which there
only exists a limited amount of parallel data, to show the potential impact of
our method in fully unsupervised machine translation. Our code, embeddings and
dictionaries are publicly available.
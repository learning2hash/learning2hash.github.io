---
layout: publication
title: Do Pretrained Contextual Language Models Distinguish Between Hebrew Homograph
  Analyses?
authors: Avi Shmidman, Cheyn Shmuel Shmidman, Dan Bareket, Moshe Koppel, Reut Tsarfaty
conference: Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics
year: 2023
bibkey: shmidman2023do
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.07099'}]
tags: ["Eacl"]
short_authors: Shmidman et al.
---
Semitic morphologically-rich languages (MRLs) are characterized by extreme
word ambiguity. Because most vowels are omitted in standard texts, many of the
words are homographs with multiple possible analyses, each with a different
pronunciation and different morphosyntactic properties. This ambiguity goes
beyond word-sense disambiguation (WSD), and may include token segmentation into
multiple word units. Previous research on MRLs claimed that standardly trained
pre-trained language models (PLMs) based on word-pieces may not sufficiently
capture the internal structure of such tokens in order to distinguish between
these analyses. Taking Hebrew as a case study, we investigate the extent to
which Hebrew homographs can be disambiguated and analyzed using PLMs. We
evaluate all existing models for contextualized Hebrew embeddings on a novel
Hebrew homograph challenge sets that we deliver. Our empirical results
demonstrate that contemporary Hebrew contextualized embeddings outperform
non-contextualized embeddings; and that they are most effective for
disambiguating segmentation and morphosyntactic features, less so regarding
pure word-sense disambiguation. We show that these embeddings are more
effective when the number of word-piece splits is limited, and they are more
effective for 2-way and 3-way ambiguities than for 4-way ambiguity. We show
that the embeddings are equally effective for homographs of both balanced and
skewed distributions, whether calculated as masked or unmasked tokens. Finally,
we show that these embeddings are as effective for homograph disambiguation
with extensive supervised training as with a few-shot setup.
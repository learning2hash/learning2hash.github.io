---
layout: publication
title: 'Learning Multilingual Word Embeddings In Latent Metric Space: A Geometric
  Approach'
authors: Pratik Jawanpuria, Arjun Balgovind, Anoop Kunchukuttan, Bamdev Mishra
conference: Transactions of the Association for Computational Linguistics
year: 2019
bibkey: jawanpuria2018learning
citations: 84
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.08773'}]
tags: ["Distance Metric Learning", "TACL"]
short_authors: Jawanpuria et al.
---
We propose a novel geometric approach for learning bilingual mappings given
monolingual embeddings and a bilingual dictionary. Our approach decouples
learning the transformation from the source language to the target language
into (a) learning rotations for language-specific embeddings to align them to a
common space, and (b) learning a similarity metric in the common space to model
similarities between the embeddings. We model the bilingual mapping problem as
an optimization problem on smooth Riemannian manifolds. We show that our
approach outperforms previous approaches on the bilingual lexicon induction and
cross-lingual word similarity tasks. We also generalize our framework to
represent multiple languages in a common latent space. In particular, the
latent space representations for several languages are learned jointly, given
bilingual dictionaries for multiple language pairs. We illustrate the
effectiveness of joint learning for multiple languages in zero-shot word
translation setting. Our implementation is available at
https://github.com/anoopkunchukuttan/geomm .
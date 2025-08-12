---
layout: publication
title: On The Language Neutrality Of Pre-trained Multilingual Representations
authors: "Jind\u0159ich Libovick\xFD, Rudolf Rosa, Alexander Fraser"
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2020'
year: 2020
bibkey: "libovick\xFD2020language"
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.05160'}]
tags: ["EMNLP"]
short_authors: "Jind\u0159ich Libovick\xFD, Rudolf Rosa, Alexander Fraser"
---
Multilingual contextual embeddings, such as multilingual BERT and
XLM-RoBERTa, have proved useful for many multi-lingual tasks. Previous work
probed the cross-linguality of the representations indirectly using zero-shot
transfer learning on morphological and syntactic tasks. We instead investigate
the language-neutrality of multilingual contextual embeddings directly and with
respect to lexical semantics. Our results show that contextual embeddings are
more language-neutral and, in general, more informative than aligned static
word-type embeddings, which are explicitly trained for language neutrality.
Contextual embeddings are still only moderately language-neutral by default, so
we propose two simple methods for achieving stronger language neutrality:
first, by unsupervised centering of the representation for each language and
second, by fitting an explicit projection on small parallel data. Besides, we
show how to reach state-of-the-art accuracy on language identification and
match the performance of statistical methods for word alignment of parallel
sentences without using parallel data.
---
layout: publication
title: Dictionary-based Debiasing Of Pre-trained Word Embeddings
authors: Masahiro Kaneko, Danushka Bollegala
conference: 'Proceedings of the 16th Conference of the European Chapter of the Association
  for Computational Linguistics: Main Volume'
year: 2021
bibkey: kaneko2021dictionary
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.09525'}]
tags: ["Eacl"]
short_authors: Masahiro Kaneko, Danushka Bollegala
---
Word embeddings trained on large corpora have shown to encode high levels of
unfair discriminatory gender, racial, religious and ethnic biases.
  In contrast, human-written dictionaries describe the meanings of words in a
concise, objective and an unbiased manner.
  We propose a method for debiasing pre-trained word embeddings using
dictionaries, without requiring access to the original training resources or
any knowledge regarding the word embedding algorithms used.
  Unlike prior work, our proposed method does not require the types of biases
to be pre-defined in the form of word lists, and learns the constraints that
must be satisfied by unbiased word embeddings automatically from dictionary
definitions of the words.
  Specifically, we learn an encoder to generate a debiased version of an input
word embedding such that it
  (a) retains the semantics of the pre-trained word embeddings,
  (b) agrees with the unbiased definition of the word according to the
dictionary, and
  (c) remains orthogonal to the vector space spanned by any biased basis
vectors in the pre-trained word embedding space.
  Experimental results on standard benchmark datasets show that the proposed
method can accurately remove unfair biases encoded in pre-trained word
embeddings, while preserving useful semantics.
---
layout: publication
title: Locality Sensitive Hashing-based Sequence Alignment Using Deep Bidirectional
  LSTM Models
authors: Neda Tavakoli
conference: Arxiv
year: 2020
bibkey: tavakoli2020locality
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.02094'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Datasets]
short_authors: Neda Tavakoli
---
Bidirectional Long Short-Term Memory (LSTM) is a special kind of Recurrent
Neural Network (RNN) architecture which is designed to model sequences and
their long-range dependencies more precisely than RNNs. This paper proposes to
use deep bidirectional LSTM for sequence modeling as an approach to perform
locality-sensitive hashing (LSH)-based sequence alignment. In particular, we
use the deep bidirectional LSTM to learn features of LSH. The obtained LSH is
then can be utilized to perform sequence alignment. We demonstrate the
feasibility of the modeling sequences using the proposed LSTM-based model by
aligning the short read queries over the reference genome. We use the human
reference genome as our training dataset, in addition to a set of short reads
generated using Illumina sequencing technology. The ultimate goal is to align
query sequences into a reference genome. We first decompose the reference
genome into multiple sequences. These sequences are then fed into the
bidirectional LSTM model and then mapped into fixed-length vectors. These
vectors are what we call the trained LSH, which can then be used for sequence
alignment. The case study shows that using the introduced LSTM-based model, we
achieve higher accuracy with the number of epochs.
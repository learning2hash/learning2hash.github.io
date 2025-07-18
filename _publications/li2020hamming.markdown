---
layout: publication
title: 'Hamming OCR: A Locality Sensitive Hashing Neural Network For Scene Text Recognition'
authors: Li et al.
conference: Arxiv
year: 2020
bibkey: li2020hamming
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.10874'}]
tags: [Locality Sensitive Hashing, DATASETS, Hashing Methods, Tools & Libraries, Evaluation]
---
Recently, inspired by Transformer, self-attention-based scene text
recognition approaches have achieved outstanding performance. However, we find
that the size of model expands rapidly with the lexicon increasing.
Specifically, the number of parameters for softmax classification layer and
output embedding layer are proportional to the vocabulary size. It hinders the
development of a lightweight text recognition model especially applied for
Chinese and multiple languages. Thus, we propose a lightweight scene text
recognition model named Hamming OCR. In this model, a novel Hamming classifier,
which adopts locality sensitive hashing (LSH) algorithm to encode each
character, is proposed to replace the softmax regression and the generated LSH
code is directly employed to replace the output embedding. We also present a
simplified transformer decoder to reduce the number of parameters by removing
the feed-forward network and using cross-layer parameter sharing technique.
Compared with traditional methods, the number of parameters in both
classification and embedding layers is independent on the size of vocabulary,
which significantly reduces the storage requirement without loss of accuracy.
Experimental results on several datasets, including four public benchmaks and a
Chinese text dataset synthesized by SynthText with more than 20,000 characters,
shows that Hamming OCR achieves competitive results.
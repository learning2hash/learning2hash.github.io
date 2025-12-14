---
layout: publication
title: 'SAFE: Self-attentive Function Embeddings For Binary Similarity'
authors: Luca Massarelli, Giuseppe Antonio di Luna, Fabio Petroni, Leonardo Querzoni,
  Roberto Baldoni
conference: Arxiv
year: 2018
bibkey: massarelli2018safe
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.05296'}]
tags: [Compact Codes, Evaluation]
short_authors: Massarelli et al.
---
The binary similarity problem consists in determining if two functions are
similar by only considering their compiled form. Advanced techniques for binary
similarity recently gained momentum as they can be applied in several fields,
such as copyright disputes, malware analysis, vulnerability detection, etc.,
and thus have an immediate practical impact. Current solutions compare
functions by first transforming their binary code in multi-dimensional vector
representations (embeddings), and then comparing vectors through simple and
efficient geometric operations. However, embeddings are usually derived from
binary code using manual feature extraction, that may fail in considering
important function characteristics, or may consider features that are not
important for the binary similarity problem. In this paper we propose SAFE, a
novel architecture for the embedding of functions based on a self-attentive
neural network. SAFE works directly on disassembled binary functions, does not
require manual feature extraction, is computationally more efficient than
existing solutions (i.e., it does not incur in the computational overhead of
building or manipulating control flow graphs), and is more general as it works
on stripped binaries and on multiple architectures. We report the results from
a quantitative and qualitative analysis that show how SAFE provides a
noticeable performance improvement with respect to previous solutions.
Furthermore, we show how clusters of our embedding vectors are closely related
to the semantic of the implemented algorithms, paving the way for further
interesting applications (e.g. semantic-based binary function search).
---
layout: publication
title: 'Asteria: Deep Learning-based Ast-encoding For Cross-platform Binary Code Similarity
  Detection'
authors: Shouguo Yang, Long Cheng, Yicheng Zeng, Zhe Lang, Hongsong Zhu, Zhiqiang
  Shi
conference: 2021 51st Annual IEEE/IFIP International Conference on Dependable Systems
  and Networks (DSN)
year: 2021
bibkey: yang2021asteria
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.06082'}]
tags: [Compact Codes, Evaluation, Datasets, Neural Hashing]
short_authors: Yang et al.
---
Binary code similarity detection is a fundamental technique for many security
applications such as vulnerability search, patch analysis, and malware
detection. There is an increasing need to detect similar code for vulnerability
search across architectures with the increase of critical vulnerabilities in
IoT devices. The variety of IoT hardware architectures and software platforms
requires to capture semantic equivalence of code fragments in the similarity
detection. However, existing approaches are insufficient in capturing the
semantic similarity. We notice that the abstract syntax tree (AST) of a
function contains rich semantic information. Inspired by successful
applications of natural language processing technologies in sentence semantic
understanding, we propose a deep learning-based AST-encoding method, named
ASTERIA, to measure the semantic equivalence of functions in different
platforms. Our method leverages the Tree-LSTM network to learn the semantic
representation of a function from its AST. Then the similarity detection can be
conducted efficiently and accurately by measuring the similarity between two
representation vectors. We have implemented an open-source prototype of
ASTERIA. The Tree-LSTM model is trained on a dataset with 1,022,616 function
pairs and evaluated on a dataset with 95,078 function pairs. Evaluation results
show that our method outperforms the AST-based tool Diaphora and
the-state-of-art method Gemini by large margins with respect to the binary
similarity detection. And our method is several orders of magnitude faster than
Diaphora and Gemini for the similarity calculation. In the application of
vulnerability search, our tool successfully identified 75 vulnerable functions
in 5,979 IoT firmware images.
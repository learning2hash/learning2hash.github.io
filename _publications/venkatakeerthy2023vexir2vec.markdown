---
layout: publication
title: 'Vexir2vec: An Architecture-neutral Embedding Framework For Binary Similarity'
authors: "S. Venkatakeerthy, Soumya Banerjee, Sayan Dey, Yashas Andaluri, Raghul Ps,\
  \ Subrahmanyam Kalyanasundaram, Fernando Magno Quint\xE3o Pereira, Ramakrishna Upadrasta"
conference: Arxiv
year: 2023
bibkey: venkatakeerthy2023vexir2vec
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.00507'}]
tags: ["Datasets", "Evaluation", "Robustness", "Tools & Libraries", "Unsupervised"]
short_authors: Venkatakeerthy et al.
---
Binary similarity involves determining whether two binary programs exhibit
similar functionality, often originating from the same source code. In this
work, we propose VexIR2Vec, an approach for binary similarity using VEX-IR, an
architecture-neutral Intermediate Representation (IR). We extract the
embeddings from sequences of basic blocks, termed peepholes, derived by random
walks on the control-flow graph. The peepholes are normalized using
transformations inspired by compiler optimizations. The VEX-IR Normalization
Engine mitigates, with these transformations, the architectural and
compiler-induced variations in binaries while exposing semantic similarities.
We then learn the vocabulary of representations at the entity level of the IR
using the knowledge graph embedding techniques in an unsupervised manner. This
vocabulary is used to derive function embeddings for similarity assessment
using VexNet, a feed-forward Siamese network designed to position similar
functions closely and separate dissimilar ones in an n-dimensional space. This
approach is amenable for both diffing and searching tasks, ensuring robustness
against Out-Of-Vocabulary (OOV) issues.
  We evaluate VexIR2Vec on a dataset comprising 2.7M functions and 15.5K
binaries from 7 projects compiled across 12 compilers targeting x86 and ARM
architectures. In diffing experiments, VexIR2Vec outperforms the nearest
baselines by \(40%\), \(18%\), \(21%\), and \(60%\) in cross-optimization,
cross-compilation, cross-architecture, and obfuscation settings, respectively.
In the searching experiment, VexIR2Vec achieves a mean average precision of
\(0.76\), outperforming the nearest baseline by \(46%\). Our framework is highly
scalable and is built as a lightweight, multi-threaded, parallel library using
only open-source tools. VexIR2Vec is \(3.1\)-\(3.5 \times\) faster than the closest
baselines and orders-of-magnitude faster than other tools.
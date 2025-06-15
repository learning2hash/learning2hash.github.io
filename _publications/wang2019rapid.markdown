---
layout: publication
title: 'Fpscreen: A Rapid Similarity Search Tool For Massive Molecular Library Based On Molecular Fingerprint Comparison'
authors: Lijun Wang, Jianbing Gong, Yingxia Zhang, Tianmou Liu, Junhui Gao
conference: "Arxiv"
year: 2019
citations: 0
bibkey: wang2019rapid
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1906.06170'}
tags: ['Retrieval Models', 'Independent', 'Cross-Modal', 'Shallow']
---
We designed a fast similarity search engine for large molecular libraries:
FPScreen. We downloaded 100 million molecules' structure files in PubChem with
SDF extension, then applied a computational chemistry tool RDKit to convert
each structure file into one line of text in MACCS format and stored them in a
text file as our molecule library. The similarity search engine compares the
similarity while traversing the 166-bit strings in the library file line by
line. FPScreen can complete similarity search through 100 million entries in
our molecule library within one hour. That is very fast as a biology
computation tool. Additionally, we divided our library into several strides for
parallel processing. FPScreen was developed in WEB mode.

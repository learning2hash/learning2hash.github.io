---
layout: publication
title: Approximate Search With Quantized Sparse Representations
authors: "Himalaya Jain, Patrick P\xE9rez, R\xE9mi Gribonval, Joaquin Zepeda, Herv\xE9\
  \ J\xE9gou"
conference: Arxiv
year: 2016
citations: 8
bibkey: jain2016approximate
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.03308'}]
tags: [ANN Search, Benchmarks and Datasets, Quantization, Evaluation Metrics]
---
This paper tackles the task of storing a large collection of vectors, such as
visual descriptors, and of searching in it. To this end, we propose to
approximate database vectors by constrained sparse coding, where possible atom
weights are restricted to belong to a finite subset. This formulation
encompasses, as particular cases, previous state-of-the-art methods such as
product or residual quantization. As opposed to traditional sparse coding
methods, quantized sparse coding includes memory usage as a design constraint,
thereby allowing us to index a large collection such as the BIGANN
billion-sized benchmark. Our experiments, carried out on standard benchmarks,
show that our formulation leads to competitive solutions when considering
different trade-offs between learning/coding time, index size and search
quality.
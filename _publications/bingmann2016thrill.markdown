---
layout: publication
title: 'Thrill: High-performance Algorithmic Distributed Batch Data Processing With
  C++'
authors: "Timo Bingmann, Michael Axtmann, Emanuel J\xF6bstl, Sebastian Lamm, Huyen\
  \ Chau Nguyen, Alexander Noe, Sebastian Schlag, Matthias Stumpp, Tobias Sturm, Peter\
  \ Sanders"
conference: 2016 IEEE International Conference on Big Data (Big Data)
year: 2016
bibkey: bingmann2016thrill
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.05634'}]
tags: ["Tools & Libraries"]
short_authors: Bingmann et al.
---
We present the design and a first performance evaluation of Thrill -- a
prototype of a general purpose big data processing framework with a convenient
data-flow style programming interface. Thrill is somewhat similar to Apache
Spark and Apache Flink with at least two main differences. First, Thrill is
based on C++ which enables performance advantages due to direct native code
compilation, a more cache-friendly memory layout, and explicit memory
management. In particular, Thrill uses template meta-programming to compile
chains of subsequent local operations into a single binary routine without
intermediate buffering and with minimal indirections. Second, Thrill uses
arrays rather than multisets as its primary data structure which enables
additional operations like sorting, prefix sums, window scans, or combining
corresponding fields of several arrays (zipping). We compare Thrill with Apache
Spark and Apache Flink using five kernels from the HiBench suite. Thrill is
consistently faster and often several times faster than the other frameworks.
At the same time, the source codes have a similar level of simplicity and
abstraction
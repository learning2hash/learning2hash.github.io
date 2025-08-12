---
layout: publication
title: Distinct Sampling On Streaming Data With Near-duplicates
authors: Jiecao Chen, Qin Zhang
conference: Proceedings of the 37th ACM SIGMOD-SIGACT-SIGAI Symposium on Principles
  of Database Systems
year: 2018
bibkey: chen2018distinct
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.12388'}]
tags: ["Datasets"]
short_authors: Jiecao Chen, Qin Zhang
---
In this paper we study how to perform distinct sampling in the streaming
model where data contain near-duplicates. The goal of distinct sampling is to
return a distinct element uniformly at random from the universe of elements,
given that all the near-duplicates are treated as the same element. We also
extend the result to the sliding window cases in which we are only interested
in the most recent items. We present algorithms with provable theoretical
guarantees for datasets in the Euclidean space, and also verify their
effectiveness via an extensive set of experiments.
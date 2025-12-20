---
layout: publication
title: A Unified Framework For Learned Sparse Retrieval
authors: Thong Nguyen, Sean MacAvaney, Andrew Yates
conference: Lecture Notes in Computer Science
year: 2023
bibkey: nguyen2023a
citations: 29
additional_links: [{name: Code, url: 'https://github.com/thongnt99/learned-sparse-retrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.13416'}]
tags: ["Efficiency", "Evaluation", "Tools & Libraries"]
short_authors: Thong Nguyen, Sean MacAvaney, Andrew Yates
---
Learned sparse retrieval (LSR) is a family of first-stage retrieval methods
that are trained to generate sparse lexical representations of queries and
documents for use with an inverted index. Many LSR methods have been recently
introduced, with Splade models achieving state-of-the-art performance on
MSMarco. Despite similarities in their model architectures, many LSR methods
show substantial differences in effectiveness and efficiency. Differences in
the experimental setups and configurations used make it difficult to compare
the methods and derive insights. In this work, we analyze existing LSR methods
and identify key components to establish an LSR framework that unifies all LSR
methods under the same perspective. We then reproduce all prominent methods
using a common codebase and re-train them in the same environment, which allows
us to quantify how components of the framework affect effectiveness and
efficiency. We find that (1) including document term weighting is most
important for a method's effectiveness, (2) including query weighting has a
small positive impact, and (3) document expansion and query expansion have a
cancellation effect. As a result, we show how removing query expansion from a
state-of-the-art model can reduce latency significantly while maintaining
effectiveness on MSMarco and TripClick benchmarks. Our code is publicly
available at https://github.com/thongnt99/learned-sparse-retrieval
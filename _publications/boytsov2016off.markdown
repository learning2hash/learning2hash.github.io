---
layout: publication
title: 'Off The Beaten Path: Let''s Replace Term-based Retrieval With K-nn Search'
authors: Leonid Boytsov, David Novak, Yury Malkov, Eric Nyberg
conference: Arxiv
year: 2016
bibkey: boytsov2016off
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.10001'}]
tags: ["Efficiency", "KDD", "Similarity Search", "Tools & Libraries"]
short_authors: Boytsov et al.
---
Retrieval pipelines commonly rely on a term-based search to obtain candidate
records, which are subsequently re-ranked. Some candidates are missed by this
approach, e.g., due to a vocabulary mismatch. We address this issue by
replacing the term-based search with a generic k-NN retrieval algorithm, where
a similarity function can take into account subtle term associations. While an
exact brute-force k-NN search using this similarity function is slow, we
demonstrate that an approximate algorithm can be nearly two orders of magnitude
faster at the expense of only a small loss in accuracy. A retrieval pipeline
using an approximate k-NN search can be more effective and efficient than the
term-based pipeline. This opens up new possibilities for designing effective
retrieval pipelines. Our software (including data-generating code) and
derivative data based on the Stack Overflow collection is available online.
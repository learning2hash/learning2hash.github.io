---
layout: publication
title: Optimistic Query Routing In Clustering-based Approximate Maximum Inner Product
  Search
authors: Sebastian Bruch, Aditya Krishnan, Franco Maria Nardini
conference: Arxiv
year: 2024
bibkey: bruch2024optimistic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.12207'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Sebastian Bruch, Aditya Krishnan, Franco Maria Nardini
---
Clustering-based nearest neighbor search is an effective method in which
points are partitioned into geometric shards to form an index, with only a few
shards searched during query processing to find a set of top-\(k\) vectors. Even
though the search efficacy is heavily influenced by the algorithm that
identifies the shards to probe, it has received little attention in the
literature. This work bridges that gap by studying routing in clustering-based
maximum inner product search. We unpack existing routers and notice the
surprising contribution of optimism. We then take a page from the sequential
decision making literature and formalize that insight following the principle
of ``optimism in the face of uncertainty.'' In particular, we present a
framework that incorporates the moments of the distribution of inner products
within each shard to estimate the maximum inner product. We then present an
instance of our algorithm that uses only the first two moments to reach the
same accuracy as state-of-the-art routers such as ScaNN by probing up to \(50%\)
fewer points on benchmark datasets. Our algorithm is also space-efficient: we
design a sketch of the second moment whose size is independent of the number of
points and requires \(\mathcal\{O\}(1)\) vectors per shard.
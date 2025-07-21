---
layout: publication
title: Scalable Similarity Search for Molecular Descriptors
authors: Tabei Yasuo, Puglisi Simon J.
conference: Journal of Chemical Information and Computer Sciences
year: 2003
bibkey: tabei2003scalable
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.10045'}]
tags: ["Similarity-Search"]
---
Similarity search over chemical compound databases is a fundamental task in
the discovery and design of novel drug-like molecules. Such databases often
encode molecules as non-negative integer vectors, called molecular descriptors,
which represent rich information on various molecular properties. While there
exist efficient indexing structures for searching databases of binary vectors,
solutions for more general integer vectors are in their infancy. In this paper
we present a time- and space- efficient index for the problem that we call the
succinct intervals-splitting tree algorithm for molecular descriptors (SITAd).
Our approach extends efficient methods for binary-vector databases, and uses
ideas from succinct data structures. Our experiments, on a large database of
over 40 million compounds, show SITAd significantly outperforms alternative
approaches in practice.
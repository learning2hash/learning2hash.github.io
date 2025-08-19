---
layout: publication
title: Faster Kernels For Graphs With Continuous Attributes Via Hashing
authors: Christopher Morris, Nils M. Kriege, Kristian Kersting, Petra Mutzel
conference: 2016 IEEE 16th International Conference on Data Mining (ICDM)
year: 2016
bibkey: morris2016faster
citations: 87
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.00064'}]
tags: [Hashing Methods, Tools & Libraries, Evaluation]
short_authors: Morris et al.
---
While state-of-the-art kernels for graphs with discrete labels scale well to
graphs with thousands of nodes, the few existing kernels for graphs with
continuous attributes, unfortunately, do not scale well. To overcome this
limitation, we present hash graph kernels, a general framework to derive
kernels for graphs with continuous attributes from discrete ones. The idea is
to iteratively turn continuous attributes into discrete labels using randomized
hash functions. We illustrate hash graph kernels for the Weisfeiler-Lehman
subtree kernel and for the shortest-path kernel. The resulting novel graph
kernels are shown to be, both, able to handle graphs with continuous attributes
and scalable to large graphs and data sets. This is supported by our
theoretical analysis and demonstrated by an extensive experimental evaluation.
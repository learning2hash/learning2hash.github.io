---
layout: publication
title: Ilp-based Local Search For Graph Partitioning
authors: Alexandra Henzinger, Alexander Noe, Christian Schulz
conference: ACM Journal of Experimental Algorithmics
year: 2020
bibkey: henzinger2018ilp
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.07144'}]
tags: ["Evaluation"]
short_authors: Alexandra Henzinger, Alexander Noe, Christian Schulz
---
Computing high-quality graph partitions is a challenging problem with
numerous applications. In this paper, we present a novel meta-heuristic for the
balanced graph partitioning problem. Our approach is based on integer linear
programs that solve the partitioning problem to optimality. However, since
those programs typically do not scale to large inputs, we adapt them to
heuristically improve a given partition. We do so by defining a much smaller
model that allows us to use symmetry breaking and other techniques that make
the approach scalable. For example, in Walshaw's well-known benchmark tables we
are able to improve roughly half of all entries when the number of blocks is
high.
---
layout: publication
title: 'Hash & Adjust: Competitive Demand-aware Consistent Hashing'
authors: Arash Pourdamghani, Chen Avin, Robert Sama, Maryam Shiran, Stefan Schmid
conference: Arxiv
year: 2024
bibkey: pourdamghani2024hash
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.11665'}]
tags: ["Hashing Methods"]
short_authors: Pourdamghani et al.
---
Distributed systems often serve dynamic workloads and resource demands evolve
over time. Such a temporal behavior stands in contrast to the static and
demand-oblivious nature of most data structures used by these systems. In this
paper, we are particularly interested in consistent hashing, a fundamental
building block in many large distributed systems. Our work is motivated by the
hypothesis that a more adaptive approach to consistent hashing can leverage
structure in the demand, and hence improve storage utilization and reduce
access time. We initiate the study of demand-aware consistent hashing. Our main
contribution is H&A, a constant-competitive online algorithm (i.e., it comes
with provable performance guarantees over time). H&A is demand-aware and
optimizes its internal structure to enable faster access times, while offering
a high utilization of storage. We further evaluate H&A empirically.
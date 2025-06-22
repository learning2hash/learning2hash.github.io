---
layout: publication
title: 'Shockhash: Towards Optimal-space Minimal Perfect Hashing Beyond Brute-force'
authors: Hans-peter Lehmann, Peter Sanders, Stefan Walzer
conference: Arxiv
year: 2023
citations: 0
bibkey: lehmann2023towards
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.09561'}]
tags: [Hashing Methods, Evaluation Metrics, Tools and Libraries]
---
A minimal perfect hash function (MPHF) maps a set \\(S\\) of \\(n\\) keys to the
first \\(n\\) integers without collisions. There is a lower bound of
\\(nlog_2e-O(log n)\\) bits of space needed to represent an MPHF. A matching
upper bound is obtained using the brute-force algorithm that tries random hash
functions until stumbling on an MPHF and stores that function's seed. In
expectation, \\(e^n\textrm\{poly\}(n)\\) seeds need to be tested. The most
space-efficient previous algorithms for constructing MPHFs all use such a
brute-force approach as a basic building block.
  In this paper, we introduce ShockHash - Small, heavily overloaded cuckoo hash
tables. ShockHash uses two hash functions \\(h_0\\) and \\(h_1\\), hoping for the
existence of a function \\(f : S \rightarrow \\{0,1\\}\\) such that \\(x \mapsto
h_\{f(x)\}(x)\\) is an MPHF on \\(S\\). In graph terminology, ShockHash generates
\\(n\\)-edge random graphs until stumbling on a pseudoforest - a graph where each
component contains as many edges as nodes. Using cuckoo hashing, ShockHash then
derives an MPHF from the pseudoforest in linear time. It uses a 1-bit retrieval
data structure to store \\(f\\) using \\(n + o(n)\\) bits.
  By carefully analyzing the probability that a random graph is a pseudoforest,
we show that ShockHash needs to try only \\((e/2)^n\textrm\{poly\}(n)\\) hash
function seeds in expectation, reducing the space for storing the seed by
roughly \\(n\\) bits. This makes ShockHash almost a factor \\(2^n\\) faster than
brute-force, while maintaining the asymptotically optimal space consumption. An
implementation within the RecSplit framework yields the currently most space
efficient MPHFs, i.e., competing approaches need about two orders of magnitude
more work to achieve the same space.
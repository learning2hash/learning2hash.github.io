---
layout: publication
title: 'Combined Search And Encoding For Seeds, With An Application To Minimal Perfect Hashing'
authors: Hans-peter Lehmann, Peter Sanders, Stefan Walzer, Jonatan Ziegler
conference: "Arxiv"
year: 2025
citations: 0
bibkey: lehmann2025combined
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2502.05613'}
tags: ['Hashing Fundamentals', 'Hashing Methods']
---
Randomised algorithms often employ methods that can fail and that are retried
with independent randomness until they succeed. Randomised data structures
therefore often store indices of successful attempts, called seeds. If \\(n\\) such
seeds are required (e.g., for independent substructures) the standard approach
is to compute for each \\(i \in [n]\\) the smallest successful seed \\(S_i\\) and store
\\(\vec\{S\} = (S_1, \ldots, S_n)\\).
  The central observation of this paper is that this is not space-optimal. We
present a different algorithm that computes a sequence \\(\vec\{S\}' = (S_1',
\ldots, S_n')\\) of successful seeds such that the entropy of \\(\vec\{S'\}\\)
undercuts the entropy of \\(\vec\{S\}\\) by \\(Ω(n)\\) bits in most cases. To
achieve a memory consumption of \\(\mathrm\{OPT\}+\epsilon n\\), the expected
number of inspected seeds increases by a factor of \\(O(1/\epsilon)\\).
  We demonstrate the usefulness of our findings with a novel construction for
minimal perfect hash functions with space requirement
\\((1+\epsilon)\mathrm\{OPT\}\\). The construction time is \\(O(n/\epsilon)\\)
while all previous approaches have construction times that increase
exponentially with \\(1/\epsilon\\). Our implementation beats the construction
throughput of the state of the art by up to two orders of magnitude.

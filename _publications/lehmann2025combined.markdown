---
layout: publication
title: Combined Search And Encoding For Seeds, With An Application To Minimal Perfect
  Hashing
authors: Lehmann et al.
conference: IEEE GLOBECOM 2008 - 2008 IEEE Global Telecommunications Conference
year: 2025
bibkey: lehmann2025combined
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.05613'}]
tags: [Hashing Methods]
---
Randomised algorithms often employ methods that can fail and that are retried with independent randomness until they succeed. Randomised data structures therefore often store indices of successful attempts, called seeds. If \\(n\\) such seeds are required (e.g., for independent substructures) the standard approach is to compute for each \\(i \in [n]\\) the smallest successful seed \\(S_i\\) and store \\(\vec\{S\} = (S_1, \ldots, S_n)\\).
  The central observation of this paper is that this is not space-optimal. We present a different algorithm that computes a sequence \\(\vec\{S\}' = (S_1', \ldots, S_n')\\) of successful seeds such that the entropy of \\(\vec\{S'\}\\) undercuts the entropy of \\(\vec\{S\}\\) by \\(Ω(n)\\) bits in most cases. To achieve a memory consumption of \\(\mathrm\{OPT\}+\epsilon n\\), the expected number of inspected seeds increases by a factor of \\(O(1/\epsilon)\\).
  We demonstrate the usefulness of our findings with a novel construction for minimal perfect hash functions that, for \\(n\\) keys and any \\(\epsilon \in [n^\{-3/7\}, 1]\\), has space requirement \\((1+\epsilon)\mathrm\{OPT\}\\) and construction time \\(O(n/\epsilon)\\). All previous approaches only support \\(\epsilon = \omega(1 / log n)\\) or have construction times that increase exponentially with \\(1/\epsilon\\). Our implementation beats the construction throughput of the state of the art by more than two orders of magnitude for \\(\epsilon \leq 3%\\).
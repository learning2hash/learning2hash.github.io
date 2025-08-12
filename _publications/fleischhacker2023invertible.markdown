---
layout: publication
title: Invertible Bloom Lookup Tables With Less Memory And Randomness
authors: Nils Fleischhacker, Kasper Green Larsen, Maciej Obremski, Mark Simkin
conference: Arxiv
year: 2024
bibkey: fleischhacker2023invertible
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.07583'}]
tags: ["Hashing Methods"]
short_authors: Fleischhacker et al.
---
In this work we study Invertible Bloom Lookup Tables (IBLTs) with small
failure probabilities. IBLTs are highly versatile data structures that have
found applications in set reconciliation protocols, error-correcting codes, and
even the design of advanced cryptographic primitives. For storing \\(n\\) elements
and ensuring correctness with probability at least \\(1 - \delta\\), existing IBLT
constructions require \\(Ω(n(\frac\{log(1/\delta)\}\{log(n)\}+1))\\) space and
they crucially rely on fully random hash functions.
  We present new constructions of IBLTs that are simultaneously more space
efficient and require less randomness. For storing \\(n\\) elements with a failure
probability of at most \\(\delta\\), our data structure only requires
\\(\mathcal\{O\}\left(n + log(1/\delta)loglog(1/\delta)\right)\\) space and
\\(\mathcal\{O\}\left(log(log(n)/\delta)\right)\\)-wise independent hash functions.
  As a key technical ingredient we show that hashing \\(n\\) keys with any \\(k\\)-wise
independent hash function \\(h:U \to [Cn]\\) for some sufficiently large constant
\\(C\\) guarantees with probability \\(1 - 2^\{-Ω(k)\}\\) that at least \\(n/2\\) keys
will have a unique hash value. Proving this is non-trivial as \\(k\\) approaches
\\(n\\). We believe that the techniques used to prove this statement may be of
independent interest.
  We apply our new IBLTs to the encrypted compression problem, recently studied
by Fleischhacker, Larsen, Simkin (Eurocrypt 2023). We extend their approach to
work for a more general class of encryption schemes and using our new IBLT we
achieve an asymptotically better compression rate.
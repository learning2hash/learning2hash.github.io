---
layout: publication
title: Invertible Bloom Lookup Tables With Less Memory And Randomness
authors: Fleischhacker Nils, Larsen Kasper Green, Obremski Maciej, Simkin Mark
conference: "Arxiv"
year: 2023
bibkey: fleischhacker2023invertible
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.07583"}
tags: ['ARXIV', 'Graph', 'Independent']
---
In this work we study Invertible Bloom Lookup Tables (IBLTs) with small failure probabilities. IBLTs are highly versatile data structures that have found applications in set reconciliation protocols, error-correcting codes, and even the design of advanced cryptographic primitives. For storing \(n\) elements and ensuring correctness with probability at least \(1 - \delta\), existing IBLT constructions require \(\Omega(n(\frac\&amp;\#123;\log(1/\delta)\&amp;\#125;\&amp;\#123;\log(n)\&amp;\#125;+1))\) space and they crucially rely on fully random hash functions. We present new constructions of IBLTs that are simultaneously more space efficient and require less randomness. For storing \(n\) elements with a failure probability of at most \(\delta\), our data structure only requires \(\mathcal\&amp;\#123;O\&amp;\#125;(n + \log(1/\delta)\log\log(1/\delta))\) space and \(\mathcal\&amp;\#123;O\&amp;\#125;(\log(\log(n)/\delta))\)-wise independent hash functions. As a key technical ingredient we show that hashing \(n\) keys with any \(k\)-wise independent hash function \(h:U \to [Cn]\) for some sufficiently large constant \(C\) guarantees with probability \(1 - 2^\&amp;\#123;-\Omega(k)\&amp;\#125;\) that at least \(n/2\) keys will have a unique hash value. Proving this is highly non-trivial as \(k\) approaches \(n\). We believe that the techniques used to prove this statement may be of independent interest.

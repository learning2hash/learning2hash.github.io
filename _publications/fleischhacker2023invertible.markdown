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
In this work we study Invertible Bloom Lookup Tables (IBLTs) with small failure probabilities. IBLTs are highly versatile data structures that have found applications in set reconciliation protocols, error-correcting codes, and even the design of advanced cryptographic primitives. For storing \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} elements and ensuring correctness with probability at least \{&#37; raw &#37;\}\\(1 - \delta\\)\{&#37; endraw &#37;\}, existing IBLT constructions require \{&#37; raw &#37;\}\\(\Omega(n(\frac\{\log(1/\delta)\}\{\log(n)\}+1))\\)\{&#37; endraw &#37;\} space and they crucially rely on fully random hash functions. We present new constructions of IBLTs that are simultaneously more space efficient and require less randomness. For storing \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} elements with a failure probability of at most \{&#37; raw &#37;\}\\(\delta\\)\{&#37; endraw &#37;\}, our data structure only requires \{&#37; raw &#37;\}\\(\mathcal\{O\}(n + \log(1/\delta)\log\log(1/\delta))\\)\{&#37; endraw &#37;\} space and \{&#37; raw &#37;\}\\(\mathcal\{O\}(\log(\log(n)/\delta))\\)\{&#37; endraw &#37;\}-wise independent hash functions. As a key technical ingredient we show that hashing \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} keys with any \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-wise independent hash function \{&#37; raw &#37;\}\\(h:U \to [Cn]\\)\{&#37; endraw &#37;\} for some sufficiently large constant \{&#37; raw &#37;\}\\(C\\)\{&#37; endraw &#37;\} guarantees with probability \{&#37; raw &#37;\}\\(1 - 2^\{-\Omega(k)\}\\)\{&#37; endraw &#37;\} that at least \{&#37; raw &#37;\}\\(n/2\\)\{&#37; endraw &#37;\} keys will have a unique hash value. Proving this is highly non-trivial as \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\} approaches \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}. We believe that the techniques used to prove this statement may be of independent interest.

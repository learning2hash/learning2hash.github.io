---
layout: publication
title: Hashing Modulo Alpha-equivalence
authors: Maziarz Krzysztof, Ellis Tom, Lawrence Alan, Fitzgibbon Andrew, Jones Simon Peyton
conference: "Arxiv"
year: 2021
bibkey: maziarz2021hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.02856"}
tags: ['ARXIV']
---
In many applications one wants to identify identical subtrees of a program syntax tree. This identification should ideally be robust to alpha-renaming of the program, but no existing technique has been shown to achieve this with good efficiency (better than \\(\mathcal&#123;O&#125;(n^2)\\) in expression size). We present a new, asymptotically efficient way to hash modulo alpha-equivalence. A key insight of our method is to use a weak (commutative) hash combiner at exactly one point in the construction, which admits an algorithm with $\mathcal{O}(n (\log n)^2)$ time complexity. We prove that the use of the commutative combiner nevertheless yields a strong hash with low collision probability. Numerical benchmarks attest to the asymptotic behaviour of the method.

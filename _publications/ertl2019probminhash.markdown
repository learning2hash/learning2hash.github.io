---
layout: publication
title: Probminhash 45;45; A Class Of Locality45;sensitive Hash Algorithms For The (probability) Jaccard Similarity
authors: Ertl Otmar
conference: "Arxiv"
year: 2019
bibkey: ertl2019probminhash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1911.00675"}
tags: ['ARXIV', 'Independent']
---
The probability Jaccard similarity was recently proposed as a natural generalization of the Jaccard similarity to measure the proximity of sets whose elements are associated with relative frequencies or probabilities. In combination with a hash algorithm that maps those weighted sets to compact signatures which allow fast estimation of pairwise similarities it constitutes a valuable method for big data applications such as near45;duplicate detection nearest neighbor search or clustering. This paper introduces a class of one45;pass locality45;sensitive hash algorithms that are orders of magnitude faster than the original approach. The performance gain is achieved by calculating signature components not independently but collectively. Four different algorithms are proposed based on this idea. Two of them are statistically equivalent to the original approach and can be used as drop45;in replacements. The other two may even improve the estimation error by introducing statistical dependence between signature components. Moreover the presented techniques can be specialized for the conventional Jaccard similarity resulting in highly efficient algorithms that outperform traditional minwise hashing and that are able to compete with the state of the art.

---
layout: publication
title: Optimal Densification For Fast And Accurate Minwise Hashing
authors: Shrivastava Anshumali
conference: "Arxiv"
year: 2017
bibkey: shrivastava2017optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.04664"}
tags: ['ARXIV', 'Independent']
---
Minwise hashing is a fundamental and one of the most successful hashing algorithm in the literature. Recent advances based on the idea of densification~\cite\{Proc:OneHashLSH\_ICML14,Proc:Shrivastava\_UAI14\} have shown that it is possible to compute \{\{ '\{\{' \}\}k\{\{ '\}\}' \}\} minwise hashes, of a vector with \{\{ '\{\{' \}\}d\{\{ '\}\}' \}\} nonzeros, in mere \{\{ '\{\{' \}\}(d + k)\{\{ '\}\}' \}\} computations, a significant improvement over the classical \{\{ '\{\{' \}\}O(dk)\{\{ '\}\}' \}\}. These advances have led to an algorithmic improvement in the query complexity of traditional indexing algorithms based on minwise hashing. Unfortunately, the variance of the current densification techniques is unnecessarily high, which leads to significantly poor accuracy compared to vanilla minwise hashing, especially when the data is sparse. In this paper, we provide a novel densification scheme which relies on carefully tailored 2-universal hashes. We show that the proposed scheme is variance-optimal, and without losing the runtime efficiency, it is significantly more accurate than existing densification techniques. As a result, we obtain a significantly efficient hashing scheme which has the same variance and collision probability as minwise hashing. Experimental evaluations on real sparse and high-dimensional datasets validate our claims. We believe that given the significant advantages, our method will replace minwise hashing implementations in practice.

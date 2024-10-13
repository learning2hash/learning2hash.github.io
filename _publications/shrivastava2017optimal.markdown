---
layout: publication
title: Optimal Densification For Fast And Accurate Minwise Hashing
authors: Shrivastava Anshumali
conference: "Arxiv"
year: 2017
bibkey: shrivastava2017optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.04664"}
tags: ['ARXIV']
---
<p>Minwise hashing is a fundamental and one of the most successful
hashing algorithm in the literature. Recent advances based on the idea
of densification~ have shown that it is possible to compute <span
class="math inline">\(k\)</span> minwise hashes, of a vector with <span
class="math inline">\(d\)</span> nonzeros, in mere <span
class="math inline">\((d + k)\)</span> computations, a significant
improvement over the classical <span
class="math inline">\(O(dk)\)</span>. These advances have led to an
algorithmic improvement in the query complexity of traditional indexing
algorithms based on minwise hashing. Unfortunately, the variance of the
current densification techniques is unnecessarily high, which leads to
significantly poor accuracy compared to vanilla minwise hashing,
especially when the data is sparse. In this paper, we provide a novel
densification scheme which relies on carefully tailored 2-universal
hashes. We show that the proposed scheme is variance-optimal, and
without losing the runtime efficiency, it is significantly more accurate
than existing densification techniques. As a result, we obtain a
significantly efficient hashing scheme which has the same variance and
collision probability as minwise hashing. Experimental evaluations on
real sparse and high-dimensional datasets validate our claims. We
believe that given the significant advantages, our method will replace
minwise hashing implementations in practice.</p>

---
layout: publication
title: Diamond Sampling For Approximate Maximum All-pairs Dot-product (MAD) Search
authors: Ballard Grey, Pinar Ali, Kolda Tamara G., Seshadhri C.
conference: "ICDM"
year: 2015
bibkey: ballard2015diamond
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1506.03872"}
tags: []
---
<p>Given two sets of vectors, <span class="math inline">\(A = \{{a_1},
\dots, {a_m}\}\)</span> and <span
class="math inline">\(B=\{{b_1},\dots,{b_n}\}\)</span>, our problem is
to find the top-<span class="math inline">\(t\)</span> dot products,
i.e., the largest <span class="math inline">\(|{a_i}\cdot{b_j}|\)</span>
among all possible pairs. This is a fundamental mathematical problem
that appears in numerous data applications involving similarity search,
link prediction, and collaborative filtering. We propose a
sampling-based approach that avoids direct computation of all <span
class="math inline">\(mn\)</span> dot products. We select diamonds
(i.e., four-cycles) from the weighted tripartite representation of <span
class="math inline">\(A\)</span> and <span
class="math inline">\(B\)</span>. The probability of selecting a diamond
corresponding to pair <span class="math inline">\((i,j)\)</span> is
proportional to <span
class="math inline">\(({a_i}\cdot{b_j})^2\)</span>, amplifying the focus
on the largest-magnitude entries. Experimental results indicate that
diamond sampling is orders of magnitude faster than direct computation
and requires far fewer samples than any competing approach. We also
apply diamond sampling to the special case of maximum inner product
search, and get significantly better results than the state-of-the-art
hashing methods.</p>

---
layout: publication
title: A Framework For Similarity Search With Space-time Tradeoffs Using Locality-sensitive Filtering
authors: Christiani Tobias
conference: "Arxiv"
year: 2016
bibkey: christiani2016framework
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.02687"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>We present a framework for similarity search based on
Locality-Sensitive Filtering (LSF), generalizing the Indyk-Motwani (STOC
1998) Locality-Sensitive Hashing (LSH) framework to support space-time
tradeoffs. Given a family of filters, defined as a distribution over
pairs of subsets of space with certain locality-sensitivity properties,
we can solve the approximate near neighbor problem in <span
class="math inline">\(d\)</span>-dimensional space for an <span
class="math inline">\(n\)</span>-point data set with query time <span
class="math inline">\(dn^{\rho_q+o(1)}\)</span>, update time <span
class="math inline">\(dn^{\rho_u+o(1)}\)</span>, and space usage <span
class="math inline">\(dn + n^{1
+ \rho_u + o(1)}\)</span>. The space-time tradeoff is tied to the
tradeoff between query time and update time, controlled by the exponents
<span class="math inline">\(\rho_q, \rho_u\)</span> that are determined
by the filter family. Locality-sensitive filtering was introduced by
Becker et al. (SODA 2016) together with a framework yielding a single,
balanced, tradeoff between query time and space, further relying on the
assumption of an efficient oracle for the filter evaluation algorithm.
We extend the LSF framework to support space-time tradeoffs and through
a combination of existing techniques we remove the oracle assumption.
Building on a filter family for the unit sphere by Laarhoven (arXiv
2015) we use a kernel embedding technique by Rahimi &amp; Recht (NIPS
2007) to show a solution to the <span
class="math inline">\((r,cr)\)</span>-near neighbor problem in <span
class="math inline">\(\ell_s^d\)</span>-space for <span
class="math inline">\(0 &lt; s
\leq 2\)</span> with query and update exponents <span
class="math inline">\(\rho_q=\frac{c^s(1+\lambda)^2}{(c^s+\lambda)^2}\)</span>
and <span
class="math inline">\(\rho_u=\frac{c^s(1-\lambda)^2}{(c^s+\lambda)^2}\)</span>
where <span class="math inline">\(\lambda\in[-1,1]\)</span> is a
tradeoff parameter. This result improves upon the space-time tradeoff of
Kapralov (PODS 2015) and is shown to be optimal in the case of a
balanced tradeoff. Finally, we show a lower bound for the space-time
tradeoff on the unit sphere that matches Laarhoven’s and our own upper
bound in the case of random data.</p>

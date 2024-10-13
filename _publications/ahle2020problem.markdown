---
layout: publication
title: On The Problem Of p_1^-1 In Locality-sensitive Hashing
authors: Ahle Thomas Dybdahl
conference: "Arxiv"
year: 2020
bibkey: ahle2020problem
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.12065"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>A Locality-Sensitive Hash (LSH) function is called <span
class="math inline">\((r,cr,p_1,p_2)\)</span>-sensitive, if two
data-points with a distance less than <span
class="math inline">\(r\)</span> collide with probability at least <span
class="math inline">\(p_1\)</span> while data points with a distance
greater than <span class="math inline">\(cr\)</span> collide with
probability at most <span class="math inline">\(p_2\)</span>. These
functions form the basis of the successful Indyk-Motwani algorithm (STOC
1998) for nearest neighbour problems. In particular one may build a
<span class="math inline">\(c\)</span>-approximate nearest neighbour
data structure with query time <span class="math inline">\(\tilde
O(n^\rho/p_1)\)</span> where <span
class="math inline">\(\rho=\frac{\log1/p_1}{\log1/p_2}\in(0,1)\)</span>.
That is, sub-linear time, as long as <span
class="math inline">\(p_1\)</span> is not too small. This is significant
since most high dimensional nearest neighbour problems suffer from the
curse of dimensionality, and can’t be solved exact, faster than a brute
force linear-time scan of the database. Unfortunately, the best LSH
functions tend to have very low collision probabilities, <span
class="math inline">\(p_1\)</span> and <span
class="math inline">\(p_2\)</span>. Including the best functions for
Cosine and Jaccard Similarity. This means that the <span
class="math inline">\(n^\rho/p_1\)</span> query time of LSH is often not
sub-linear after all, even for approximate nearest neighbours! In this
paper, we improve the general Indyk-Motwani algorithm to reduce the
query time of LSH to <span class="math inline">\(\tilde
O(n^\rho/p_1^{1-\rho})\)</span> (and the space usage correspondingly.)
Since <span class="math inline">\(n^\rho p_1^{\rho-1} &lt; n
\Leftrightarrow p_1 &gt; n^{-1}\)</span>, our algorithm always obtains
sublinear query time, for any collision probabilities at least <span
class="math inline">\(1/n\)</span>. For <span
class="math inline">\(p_1\)</span> and <span
class="math inline">\(p_2\)</span> small enough, our improvement over
all previous methods can be in both query time and space. The
improvement comes from a simple change to the Indyk-Motwani algorithm,
which can easily be implemented in existing software packages.</p>

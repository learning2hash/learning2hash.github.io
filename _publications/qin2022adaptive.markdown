---
layout: publication
title: Adaptive And Dynamic Multi-resolution Hashing For Pairwise Summations
authors: Qin Lianke, Reddy Aravind, Song Zhao, Xu Zhaozhuo, Zhuo Danyang
conference: "Arxiv"
year: 2022
bibkey: qin2022adaptive
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2212.11408"}
tags: ['ARXIV', 'Independent']
---
<p>In this paper, we propose Adam-Hash: an adaptive and dynamic
multi-resolution hashing data-structure for fast pairwise summation
estimation. Given a data-set <span class="math inline">\(X \subset
\mathbb{R}^d\)</span>, a binary function <span
class="math inline">\(f:\mathbb{R}^d\times
\mathbb{R}^d\to \mathbb{R}\)</span>, and a point <span
class="math inline">\(y \in \mathbb{R}^d\)</span>, the Pairwise
Summation Estimate <span class="math inline">\(\mathrm{PSE}_X(y) :=
\frac{1}{|X|} \sum_{x \in X} f(x,y)\)</span>. For any given data-set
<span class="math inline">\(X\)</span>, we need to design a
data-structure such that given any query point <span
class="math inline">\(y \in \mathbb{R}^d\)</span>, the data-structure
approximately estimates <span
class="math inline">\(\mathrm{PSE}_X(y)\)</span> in time that is
sub-linear in <span class="math inline">\(|X|\)</span>. Prior works on
this problem have focused exclusively on the case where the data-set is
static, and the queries are independent. In this paper, we design a
hashing-based PSE data-structure which works for the more practical
setting in which insertions, deletions, and replacements of points are
allowed. Moreover, our proposed Adam-Hash is also robust to adaptive PSE
queries, where an adversary can choose query <span
class="math inline">\(q_j \in \mathbb{R}^d\)</span> depending on the
output from previous queries <span class="math inline">\(q_1, q_2,
\dots, q_{j-1}\)</span>.</p>

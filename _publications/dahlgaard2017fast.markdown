---
layout: publication
title: Fast Similarity Sketching
authors: Dahlgaard Søren, Langhede Mathias Bæk Tejs, Houen Jakob Bæk Tejs, Thorup Mikkel
conference: "Arxiv"
year: 2017
bibkey: dahlgaard2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.04370"}
tags: ['ARXIV', 'Supervised']
---
<p>We consider the <span class="math inline">\(\textit{Similarity
Sketching}\)</span> problem: Given a universe <span
class="math inline">\([u] = \{0,\ldots, u-1\}\)</span> we want a random
function <span class="math inline">\(S\)</span> mapping subsets <span
class="math inline">\(A\subseteq [u]\)</span> into vectors <span
class="math inline">\(S(A)\)</span> of size <span
class="math inline">\(t\)</span>, such that the Jaccard similarity <span
class="math inline">\(J(A,B) = |A\cap B|/|A\cup B|\)</span> between sets
<span class="math inline">\(A\)</span> and <span
class="math inline">\(B\)</span> is preserved. More precisely, define
<span class="math inline">\(X_i = [S(A)[i] =
  S(B)[i]]\)</span> and <span class="math inline">\(X = \sum_{i\in [t]}
X_i\)</span>. We want <span
class="math inline">\(E[X_i]=J(A,B)\)</span>, and we want <span
class="math inline">\(X\)</span> to be strongly concentrated around
<span class="math inline">\(E[X] = t \cdot J(A,B)\)</span> (i.e.
Chernoff-style bounds). This is a fundamental problem which has found
numerous applications in data mining, large-scale classification,
computer vision, similarity search, etc. via the classic MinHash
algorithm. The vectors <span class="math inline">\(S(A)\)</span> are
also called <span class="math inline">\(\textit{sketches}\)</span>.
Strong concentration is critical, for often we want to sketch many sets
<span class="math inline">\(B_1,\ldots,B_n\)</span> so that we later,
for a query set <span class="math inline">\(A\)</span>, can find (one
of) the most similar <span class="math inline">\(B_i\)</span>. It is
then critical that no <span class="math inline">\(B_i\)</span> looks
much more similar to <span class="math inline">\(A\)</span> due to
errors in the sketch. The seminal <span
class="math inline">\(t\times\textit{MinHash}\)</span> algorithm uses
<span class="math inline">\(t\)</span> random hash functions <span
class="math inline">\(h_1,\ldots, h_t\)</span>, and stores <span
class="math inline">\(\left ( \min_{a\in A} h_1(A),\ldots,
\min_{a\in A} h_t(A) \right )\)</span> as the sketch of <span
class="math inline">\(A\)</span>. The main drawback of MinHash is,
however, its <span class="math inline">\(O(t\cdot |A|)\)</span> running
time, and finding a sketch with similar properties and faster running
time has been the subject of several papers. (continued…)</p>

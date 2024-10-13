---
layout: publication
title: Quicksort Largest Bucket And Min-wise Hashing With Limited Independence
authors: Knudsen Mathias Bæk Tejs, Stöckel Morten
conference: "Arxiv"
year: 2015
bibkey: knudsen2015quicksort
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1502.05729"}
tags: ['ARXIV', 'Independent']
---
<p>Randomized algorithms and data structures are often analyzed under
the assumption of access to a perfect source of randomness. The most
fundamental metric used to measure how “random” a hash function or a
random number generator is, is its independence: a sequence of random
variables is said to be <span
class="math inline">\(k\)</span>-independent if every variable is
uniform and every size <span class="math inline">\(k\)</span> subset is
independent. In this paper we consider three classic algorithms under
limited independence. We provide new bounds for randomized quicksort,
min-wise hashing and largest bucket size under limited independence. Our
results can be summarized as follows. -Randomized quicksort. When pivot
elements are computed using a <span
class="math inline">\(5\)</span>-independent hash function, Karloff and
Raghavan, J.ACM’93 showed <span class="math inline">\(O ( n
\log n)\)</span> expected worst-case running time for a special version
of quicksort. We improve upon this, showing that the same running time
is achieved with only <span
class="math inline">\(4\)</span>-independence. -Min-wise hashing. For a
set <span class="math inline">\(A\)</span>, consider the probability of
a particular element being mapped to the smallest hash value. It is
known that <span class="math inline">\(5\)</span>-independence implies
the optimal probability <span class="math inline">\(O (1 /n)\)</span>.
Broder et al., STOC’98 showed that <span
class="math inline">\(2\)</span>-independence implies it is <span
class="math inline">\(O(1 / \sqrt{|A|})\)</span>. We show a matching
lower bound as well as new tight bounds for <span
class="math inline">\(3\)</span>- and <span
class="math inline">\(4\)</span>-independent hash functions. -Largest
bucket. We consider the case where <span
class="math inline">\(n\)</span> balls are distributed to <span
class="math inline">\(n\)</span> buckets using a <span
class="math inline">\(k\)</span>-independent hash function and analyze
the largest bucket size. Alon et. al, STOC’97 showed that there exists a
<span class="math inline">\(2\)</span>-independent hash function
implying a bucket of size <span class="math inline">\(\Omega (
n^{1/2})\)</span>. We generalize the bound, providing a <span
class="math inline">\(k\)</span>-independent family of functions that
imply size <span class="math inline">\(\Omega
( n^{1/k})\)</span>.</p>

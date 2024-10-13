---
layout: publication
title: Cuckoo Hashing In Cryptography Optimal Parameters Robustness And Applications
authors: Yeo Kevin
conference: "Arxiv"
year: 2023
bibkey: yeo2023cuckoo
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.11220"}
tags: ['ARXIV', 'Graph', 'Independent']
---
<p>Cuckoo hashing is a powerful primitive that enables storing items
using small space with efficient querying. At a high level, cuckoo
hashing maps <span class="math inline">\(n\)</span> items into <span
class="math inline">\(b\)</span> entries storing at most <span
class="math inline">\(\ell\)</span> items such that each item is placed
into one of <span class="math inline">\(k\)</span> randomly chosen
entries. Additionally, there is an overflow stash that can store at most
<span class="math inline">\(s\)</span> items. Many cryptographic
primitives rely upon cuckoo hashing to privately embed and query data
where it is integral to ensure small failure probability when
constructing cuckoo hashing tables as it directly relates to the privacy
guarantees. As our main result, we present a more query-efficient cuckoo
hashing construction using more hash functions. For construction failure
probability <span class="math inline">\(\epsilon\)</span>, the query
overhead of our scheme is <span class="math inline">\(O(1 +
\sqrt{\log(1/\epsilon)/\log n})\)</span>. Our scheme has quadratically
smaller query overhead than prior works for any target failure
probability <span class="math inline">\(\epsilon\)</span>. We also prove
lower bounds matching our construction. Our improvements come from a new
understanding of the locality of cuckoo hashing failures for small sets
of items. We also initiate the study of robust cuckoo hashing where the
input set may be chosen with knowledge of the hash functions. We present
a cuckoo hashing scheme using more hash functions with query overhead
<span class="math inline">\(\tilde{O}(\log \lambda)\)</span> that is
robust against poly<span class="math inline">\((\lambda)\)</span>
adversaries. Furthermore, we present lower bounds showing that this
construction is tight and that extending previous approaches of large
stashes or entries cannot obtain robustness except with <span
class="math inline">\(\Omega(n)\)</span> query overhead. As applications
of our results, we obtain improved constructions for batch codes and
PIR. In particular, we present the most efficient explicit batch code
and blackbox reduction from single-query PIR to batch PIR.</p>
